from sqlalchemy import Column, String, Integer

from  model import Base

class Animalzinho(Base):
    __tablename__ = 'animalzinho'

    id = Column("pk_animalzinho", Integer, primary_key=True)
    nome = Column(String(140))
    especie = Column(String(140))
    raca = Column(String(140))
    idade = Column(Integer)
    descricao = Column(String(140))