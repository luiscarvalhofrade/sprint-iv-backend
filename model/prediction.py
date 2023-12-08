from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from typing import Union

from  model import Base

class Prediction(Base):
    __tablename__ = 'prediction'

    id = Column("pk_prediction", Integer, primary_key=True)
    bwt = Column(Integer)
    gestation = Column(Integer)
    parity = Column(Integer)
    age = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    smoke = Column(Integer)
    date_insertion = Column(DateTime, default=datetime.now())

    def __init__(self, bwt:int, gestation:int, parity:int,
                 age:int, weight:int, height:int, smoke:int,
                 date_insertion:Union[DateTime, None] = None):
        """
        Cria uma Predição

        Arguments:
            bwt: peso do bebê em onças
            gestation: total de dias da gestação
            parity: caso 1 primogenito, caso 0 uma ou mais gestações anteriores
            age: idade da mãe
            weight: peso da mãe em libras
            height: altura da mãe em inches
            smoke: predição se a mãe fumou durante a gestação. Caso 1 a mãe fumou durante a gestação, caso 0 não fumou durante a gestação
            date_insertion: data de quando a predição foi inserido à base
        """
        self.bwt = bwt
        self.gestation = gestation
        self.parity = parity
        self.age = age
        self.weight = weight
        self.height = height
        self.smoke = smoke

        # se não for informada, será o data exata da inserção no banco
        if date_insertion:
            self.date_insertion = date_insertion