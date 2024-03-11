from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///salaries.db", connect_args={"check_same_thread": False})
session_local = sessionmaker(engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)

def get_db() :
    db = session_local()

    try:
        yield db
    finally:
        db.close()
