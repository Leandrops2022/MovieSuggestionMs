from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__="filmes"

    id = Column(Integer, primary_key=True, index=True)
    titulo_portugues = Column(String, nullable=False)
    ano_lancamento = Column(Integer)
    nota = Column(Float)
    genres = Column(String)
    quantidade_de_votos = Column(Integer)


