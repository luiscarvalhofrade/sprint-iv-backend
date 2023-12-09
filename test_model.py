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

# Carga dos dados
dataset = loader.data_loader(url_data, columns)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]

# Método para testar modelo SVM a partir do arquivo correspondente
def test_model_svm():
    # Importando modelo de SVM
    svm_path = './smoker_preditor_svm.pkl'

    model_svm = Model.load_model(svm_path)

    # Obtendo as métricas do KNN
    accuracy_svm = evaluator.valuation(model_svm, X, Y)
    
    # Testando as métricas do SVM
    assert accuracy_svm >= 0.6