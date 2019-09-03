from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()



def init_db():
    engine = create_engine('sqlite:///memory')
    conn = engine.connect()


if __name__ == '__main__':
    init_db()