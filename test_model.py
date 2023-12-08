import pytest
import pandas as pd
from utils.model import run_prediction
from model.base import Base
import pickle

def test_model():
    bwt=  125,
    gestation= 280,
    parity= 0,
    age= 30,
    weight= 100,
    height= 69.0,

    input_for_model = {
        
                'bwt':  bwt,
                'gestation': gestation,
                'parity': parity,
                'age': age,
                'weight': weight,
                'height': height,
        }
    atributos = ['bwt', 'gestation', 'parity', 'age', 'weight', 'height']
    
    entrada = pd.DataFrame(input_for_model, columns=atributos)
    result = run_prediction(entrada)
    assert result == 1

def test_accuracy_threshold():
    pickle_in = open('./utils/smoker_preditor.pkl', 'rb')
    model = pickle.load(pickle_in)
    model.predict(rescaledTestX)
    accuracy_score(predictions)