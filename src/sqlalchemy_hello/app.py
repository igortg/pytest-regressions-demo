from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
Session = None

def init_db():
    engine = create_engine('sqlite://')
    conn = engine.connect()
    Base.metadata.create_all(bind=conn)
    global Session
    session_maker = sessionmaker(bind=conn)
    Session = scoped_session(session_maker)


def db_session():
    if not Session:
        raise RuntimeError("Call init_db")
    return Session()
