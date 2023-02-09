from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from dataConversion import readPDF
import os
from dataConversion import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/temp_files' 

def remove_temp_files():
    temp_files = os.listdir('static/temp_files')
    for file in temp_files:
          os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))

@app.route('/')
def index():
    return render_template("admin.html")


@app.route('/upload', methods=['POST'])
def upload_file():
    remove_temp_files()

    file_upload = request.files['Resume']
    file_upload.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file_upload.filename)))
    return redirect('/result')


@app.route('/result')
def display_result():
    uploadedFile = os.listdir('static/temp_files')
    if len(uploadedFile) == 0:
        return redirect('/')
    
    skills, educations = readPDF('./static/temp_files/' + uploadedFile[0])
    return render_template('result.html', skills=skills, educations=educations)

if __name__ == "__main__":
    app.run(debug=True)