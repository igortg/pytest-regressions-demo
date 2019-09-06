import pprint

from serialchemy.func import dump
from sqlalchemy_hello.app import init_db
from sqlalchemy_hello.player_char import Espada, PlayerChar, ClasseChar, RacaChar

session = init_db()

espada_nilfgaardian = Espada(nome="Nilfgaardian longsword", dano=36, min_level=3)

character = PlayerChar(
    nome="Yennefer",
    classe=ClasseChar.Xama,
    raca=RacaChar.Human,
    forca=9,
    habilidade=14,
    resistencia=13,
    inteligencia=16,
    level=4,
    arma_primaria=espada_nilfgaardian
)

session.add(character)
session.commit()

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(dump(character, nest_foreign_keys=True))
