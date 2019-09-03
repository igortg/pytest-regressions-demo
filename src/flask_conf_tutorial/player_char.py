import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, Float, Enum

from .app import Base


class ClasseChar(enum.Enum):
    Guerreiro = 1
    Paladino = 2
    Xama = 3
    Druida = 4
    Mago = 5


class RacaChar(enum.Enum):
    Human = enum.auto()
    Elf = enum.auto()
    Orc = enum.auto()


class PlayerChar(Base):
    __tablename__ = 'PlayerChar'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    raca = Column(Enum(RacaChar))
    classe = Column(Enum(ClasseChar))
    # Level
    pontos_xp = Column(Integer, default=0)
    level = Column(Integer, default=0)
    # Atributos
    forca = Column(Float, default=10)
    habilidade = Column(Float, default=10)
    resistencia = Column(Float, default=10)
    inteligencia = Column(Float, default=10)
    # Atributos derivados
    pontos_de_vida = Column(Integer)
    pontos_de_mana = Column(Integer)
    modificador_espada = Column(Float)
    modificador_machado = Column(Float)
    modificador_arco = Column(Float)
    #
    data_criacao = Column(Date, default=datetime.now())
    data_ultimo_level_up = Column(Date)

    def level_up(self):
        self.level += 1
        if self.classe == ClasseChar.Xama:
            self.inteligencia *= 1.2
            self.habilidade *= 1.15
            self.forca *= 1.05
            self.resistencia *= 1.08
        self.pontos_de_vida = self.inteligencia * 100
        self.pontos_de_mana = self.inteligencia * 76
        if self.raca == RacaChar.Human:
            self.modificador_espada = min(self.forca, self.habilidade) * 0.02
            self.modificador_machado = self.forca * 0.03
            self.modificador_arco = self.habilidade * 0.04

        self.data_ultimo_level_up = datetime.now()
