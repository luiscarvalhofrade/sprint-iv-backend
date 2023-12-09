from utils.evaluator import Evaluator
from utils.loader import Loader
from utils.model import Model
from utils.preprocessor import PreProcessor

# To run: pytest -v test_modelos.py

# Instanciação das Classes
loader = Loader()
model = Model()
evaluator = Evaluator()
pre_processor = PreProcessor()

# Parâmetros    
url_data = "./babies.csv"
columns = ['bwt', 'parity', 'gestation', 'age', 'height', 'weight', 'smoke']
percentual_test = 0.3

# Carga dos dados
dataset = loader.data_loader(url_data, columns)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
"""
def test_modelo_lr():  
    # Importando o modelo de regressão logística
    lr_path = 'ml_model/diabetes_lr.pkl'
    modelo_lr = model.load_model(lr_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_lr, recall_lr, precisao_lr, f1_lr = evaluator.valuation(modelo_lr, X, Y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_lr >= 0.75 
    assert recall_lr >= 0.5 
    assert precisao_lr >= 0.5 
    assert f1_lr >= 0.5 

"""
# Método para testar modelo SVM a partir do arquivo correspondente
def test_model_svm():
    # Importando modelo de SVM
    svm_path = './smoker_preditor.pkl'

    model_svm = Model.load_model(svm_path)

    # Obtendo as métricas do KNN
    acuracia_svm, recall_svm, precision_svm, f1_svm = evaluator.valuation(model_svm, X, Y)
    
    # Testando as métricas do KNN
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_svm >= 0.6
    assert recall_svm >= 0.5 
    assert precision_svm >= 0.5 
    assert f1_svm >= 0.5 
    