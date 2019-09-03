from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, Float

from .app import Base


class Empregado(Base):
    __tablename__ = 'Empregado'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    sobrenome = Column(String)
    email = Column(String)
    admissao = Column(Date)
    salario = Column(Float)
    data_ultimo_pgto = Column(Date)
    total_recebido = Column(Float, default=0)
    inss_devido = Column(Float, default=0)
    decimo_terceiro = Column(Float, default=0)

    def processa_pagamento(self):
        self.data_ultimo_pgto = datetime.now()
        self.total_recebido += self.salario
        self.inss_devido += self.salario * 0.08
        self.decimo_terceiro += self.salario / 12
