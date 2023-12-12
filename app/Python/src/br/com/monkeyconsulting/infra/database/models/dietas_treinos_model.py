from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DietaTreinoModel(Base):
    __tablename__ = 'DIETAS_TREINOS'

    id_dieta = Column(Integer, primary_key=True)
    descricao = Column(String)

    def __repr__(self):
        return f"<Dieta/Treino(descricao'{self.descricao}'>"

    def to_model(self, dto):
        self.descricao = dto.get('descricao')
        self.id_dieta = dto.get('id_dieta')
        return self

    def __init__(self, *args, **keyword):
        super().__init__(*args, **keyword)
