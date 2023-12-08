from pydantic import BaseModel
from typing import List
from model.prediction import Prediction


class PredictionSchema(BaseModel):
    """ Define os dados a serem inseridos pelo usuário
    """
    bwt: int = 120
    gestation: int = 284
    parity: int = 1
    age: int = 23
    weight: int = 100
    height: int = 63

class PredictionViewSchema(BaseModel):
    """ Define como uma nova predição a ser inserida deve ser representada
    """
    bwt: int = 120
    gestation: int = 284
    parity: int = 1
    age: int = 23
    weight: int = 100
    height: int = 63
    smoke: int = 0

class PredictionsListSchema(BaseModel):
    """ Define como uma listagem de predições será retornada.
    """
    predictions:List[PredictionViewSchema]


def show_predictions(predictions: List[Prediction]):
    """ Retorna uma representação das predições seguindo o schema definido em
        PredictionViewSchema.
    """
    result = []
    for prediction in predictions:
        result.append({
            "bwt": prediction.bwt,
            "gestation": prediction.gestation,
            "parity": prediction.parity,
            "age": prediction.age,
            "height": prediction.height,
            "weight": prediction.weight,
            "smoke": prediction.smoke,
        })

    return {"predictions": result}

def show_prediction(prediction: Prediction):
    """ Retorna uma representação da predição seguindo o schema definido em
        PredcitionViewSchema.
    """
    return {
        "id": prediction.id,
        "bwt": prediction.bwt,
        "gestation": prediction.gestation,
        "parity": prediction.parity,
        "age": prediction.age,
        "height": prediction.height,
        "weight": prediction.weight,
        "smoke": prediction.smoke,
    }

