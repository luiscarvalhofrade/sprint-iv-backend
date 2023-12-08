import numpy as np
from sklearn import datasets
import pickle
import joblib

class Model:

    def load_model(path):

        #carregando o modelo treinado independente se é pickle ou joblib
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model


    #definindo o metodo que roda a predição com os dados a serem inputados
    def run_prediction(model, form):

        X_input = np.array([
            form.bwt,
            form.gestation,
            form.parity,
            form.age,
            form.weight,
            form.height
        ])
        
        #utilizando o modelo para fazer uma predição
        prediction_result = model.predict(X_input.reshape(1, -1))
        
        #retrorna a predição
        return int(prediction_result[0])