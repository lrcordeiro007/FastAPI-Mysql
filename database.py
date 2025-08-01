from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql 


URL_DATABASE= 'mysql+pymysql://{seu-nome}:{sua-senha}@localhost:3306/BlogApplication'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker (autocommit=False, autoflush=False , bind= engine)

Base = declarative_base()
