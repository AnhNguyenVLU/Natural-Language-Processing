from flask import Flask, render_template, request
import torch
import pickle
from model import *
from attacut import tokenize, Tokenizer
from torchtext.data.utils import get_tokenizer

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
SEED = 1234
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True

variants = 'additive'
save_path = './models/Seq2SeqAttention_additive.pt'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
app.config['UPLOAD_FOLDER'] = 'static/files'

SRC_LANGUAGE, TRG_LANGUAGE = 'spa', 'en'

token_transform = {}
token_transform[SRC_LANGUAGE] = Tokenizer(model="attacut-sc")
token_transform[TRG_LANGUAGE] = get_tokenizer('spacy', language='en_core_web_sm')

UNK_IDX, PAD_IDX, SOS_IDX, EOS_IDX = 0, 1, 2, 3
special_symbols = ['<unk>', '<pad>', '<sos>', '<eos>']

with open('vocab_transform.pickle', 'rb') as handle:
    vocab_transform = pickle.load(handle)

def sequential_transforms(*transforms):
    def func(txt_input):
        for transform in transforms:
            if transform == token_transform[SRC_LANGUAGE]:
                txt_input = transform.tokenize(txt_input)
            else:
                txt_input = transform(txt_input)
        return txt_input
    return func

def tensor_transform(token_ids):
    return torch.cat((torch.tensor([SOS_IDX]), 
                      torch.tensor(token_ids), 
                      torch.tensor([EOS_IDX])))

text_transform = {}
for ln in [SRC_LANGUAGE, TRG_LANGUAGE]:
    text_transform[ln] = sequential_transforms(token_transform[ln], vocab_transform[ln], tensor_transform)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mt', methods=['GET', 'POST'])
def machine_translation():
    if request.method == 'POST':
        source = request.form.get('source')
        predict = translation(source, variants, save_path, device)
    else:
        source = ''
        predict = ''
    data = {"source": source, "predict": predict}
    return render_template("lab.html", data=data)

def translation(source, variants, save_path, device):
    src_text = text_transform[SRC_LANGUAGE](source).to(device)
    target = "It is fake target"*20
    trg_text = text_transform[TRG_LANGUAGE](target).to(device)
    trg_text = trg_text.reshape(-1, 1)
    src_text = src_text.reshape(-1, 1) 

if __name__ == "__main__":
    app.run(debug=True)
