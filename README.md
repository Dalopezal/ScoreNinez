### Deep learning project seed
Use this seed to start new deep learning / ML projects.

- Built in setup.py
- Built in requirements
- Examples with MNIST
- Badges
- Bibtex

#### Objetivos  
Este repositorio genera un score para los niños del valle del cauca  y los municipios del norte del cauca teniendo en cuenta 5 dimensiones

    *   Bienestar Material
    *   Cuidado
    *   Educación
    *   Salud
    *   Seguridad 

### DELETE EVERYTHING ABOVE FOR YOUR PROJECT  
 
---

<div align="center">    
 
# Score Primera Infancia   

[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/NeurIPS-2019-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)
[![Conference](http://img.shields.io/badge/ICLR-2019-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)  
<!--
ARXIV   
[![Paper](http://img.shields.io/badge/arxiv-math.co:1480.1111-B31B1B.svg)](https://www.nature.com/articles/nature14539)
-->
![CI testing](https://github.com/PyTorchLightning/deep-learning-project-template/workflows/CI%20testing/badge.svg?branch=master&event=push)


<!--  
Conference   
-->   
</div>
 
## Description   
What it does   

## How to run Models
First, install dependencies   
```bash
# clone project   
git clone https://github.com/Dalopezal/ScoreNinez

# install project   
cd DimensionInfancias 
cd Models
pip install --upgrade pip
pip install -r requirements.txt
 ```   
 Next, navigate to any file and run it.   
 ```bash
# module folder
cd project

# run module (example: mnist as your main contribution)   
python lit_classifier_main.py    
```

## Imports
This project is setup as a package which means you can now easily import any file into any other file like so:
```python
from project.datasets.mnist import mnist
from project.lit_classifier_main import LitClassifier
from pytorch_lightning import Trainer

# model
model = LitClassifier()

# data
train, val, test = mnist()

# train
trainer = Trainer()
trainer.fit(model, train, val)

# test using the best model!
trainer.test(test_dataloaders=test)
```


## How to run Front


```bash
cd Front
```
and run the server with one of the following command
```bash
python -m http.server 8000
php -S localhost:8000
```


## How

to run the models using virtualenv


```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```