from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from com.monkeyconsulting.domain.dtos.dieta_treino_dto import DietaTreinoDTO

Base = declarative_base()


class DietaTreinoModel(Base):
    __tablename__ = 'DIETAS_TREINOS'

    id_dieta = Column(Integer, primary_key=True)
    descricao = Column(String)

    def to_model(self, dto):
        self.descricao = dto.get('descricao')
        self.id_dieta = dto.get('id_dieta')
        return self

    def to_dto(self):
        dto = DietaTreinoDTO()
        dto.id_dieta = self.id_dieta
        dto.descricao = self.descricao
        return dto

    def __repr__(self):
        return f"<Dieta/Treino(descricao'{self.descricao}'>"

    def __init__(self, *args, **keyword):
        super().__init__(*args, **keyword)
