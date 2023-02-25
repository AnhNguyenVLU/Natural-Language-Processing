## READING PAPER NLP
### Paper 3: Type-Driven Multi-Turn Corrections for Grammatical Error Correction
Link paper: https://aclanthology.org/2022.findings-acl.254 \
Date: 25/02/2023
| Topic        |          Type-Driven Multi-Turn Corrections for Grammatical Error Correction          |
|--------------|--------------------------------------------------------------------------------------------------------|
| Question Reserch   | In what way is the author's model trained to not only fix errors incrementally, but also exploit interdependencies between different types of errors for better performance?|
| Related Work |  - There are two categories of models in GEC: Transformer-dominant NMT-based models and GECToR-leading Seq2Label models <br /> - By comparison, Seq2Label models are able to correct grammatical errors more efficiently and even better. <br /> - Since GEC models may fail to completely correct a sentence through just one-iteration inference, some researchers resort to data augmentation that has been widely used in other NLP studies |
| Solution     | Using this TypeDriven Multi-Turn Corrections, from each training instance, author additionally construct multiple training instances, each of which involves the correction of a specific type of errors. Then, author use these additionally-constructed training instances and the original one to train the model in turn. |
| Method       | |
| Result       | A TypeDriven Multi-Turn Corrections approach for GEC show that significantly benefits the model training and  enhanced model achieves state-of-the-art single-model performance on English GEC benchmarks. |

