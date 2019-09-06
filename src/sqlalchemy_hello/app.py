from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def init_db():
    engine = create_engine('sqlite://')
    conn = engine.connect()
    Base.metadata.create_all(bind=conn)
    Session = sessionmaker(bind=conn)
    return Session()
