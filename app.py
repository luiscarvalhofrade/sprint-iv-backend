from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from utils import *
import warnings
warnings.filterwarnings("ignore")

from sqlalchemy.exc import IntegrityError

from model import Session, Prediction
#from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
prediction_tag = Tag(name="Predicition", description="Adição e visualização de predições à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/predictions', tags=[prediction_tag],
          responses={"200": PredictionViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_data(form: PredictionSchema):
    """Roda uma predição com os dados inputados e adiciona à base de dados
        
    Atributos = ['bwt', 'gestation', 'parity', 'age', 'weight', 'height']

    Retorna uma representação da predição.
    """
    
    path = './smoker_preditor.pkl'
    modelo = Model.load_model(path)

    prediction = Prediction(
        bwt=form.bwt,
        gestation=form.gestation,
        parity=form.parity,
        age=form.age,
        height=form.height,
        weight=form.weight,
        smoke=Model.run_prediction(modelo, form))
    
    #logger.debug(f"Adicionando predição: '{prediction.id}'")
    try:
        # criando conexão com a base
        session = Session()

        # adicionando produto
        session.add(prediction)
        
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        #logger.debug(f"Adicionado predição: '{prediction.id}'")
        
        return show_prediction(prediction), 200

    except IntegrityError as e:
        # evita duplicidade
        error_msg = "Predição com os mesmos dados já salvo na base :/"
        #logger.warning(f"Erro ao rodar predição '{prediction.id}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível rodar nova predição :/"
        #logger.warning(f"Erro ao adicionar nova predição '{prediction.id}', {error_msg}")
        return {"mesage": error_msg}, 400
    

@app.get('/predictions', tags=[prediction_tag],
         responses={"200": PredictionsListSchema, "404": ErrorSchema})
def get_prediction():
    """Faz a busca por todos as predições já salvas

    Retorna uma representação da listagem de predições.
    """
    #logger.debug(f"Coletando predições ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    predictions = session.query(Prediction).all()

    if not predictions:
        # se não há produtos cadastrados
        return {"predições": []}, 200
    else:
        #logger.debug(f"%d predições econtrados" % len(predictions))
        # retorna a representação de produto
        print(predictions)
        return show_predictions(predictions), 200
