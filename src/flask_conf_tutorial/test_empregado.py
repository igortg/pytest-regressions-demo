import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask_conf_tutorial.app import Base
from flask_conf_tutorial.empregado import Empregado


@pytest.fixture
def session():
    engine = create_engine('sqlite:///memory')
    conn = engine.connect()
    Base.metadata.create_all(bind=conn)
    Session = sessionmaker(bind=conn)
    yield Session()
    conn.close()


def test_processa_pagamento(session):
    empregado = Empregado(nome="Maria", sobrenome="Dumont", salario=3000)
    session.add(empregado)
    session.commit()

    empregado.processa_pagamento()





