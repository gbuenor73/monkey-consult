from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from com.monkeyconsulting.domain.dtos.plano_dto import PlanoDTO

Base = declarative_base()


class PlanoModel(Base):
    __tablename__ = 'PLANOS'

    id_plano = Column(Integer, primary_key=True)
    dias_para_vencimento = Column(Integer)
    dias_para_troca_da_dieta = Column(Integer)
    descricao = Column(String)

    def to_model(self, dto):
        self.dias_para_vencimento = dto.get('dias_para_vencimento')
        self.dias_para_troca_da_dieta = dto.get('dias_para_troca_da_dieta')
        self.descricao = dto.get('descricao')
        return self

    def to_dto(self):
        dto = PlanoDTO()
        dto.dias_para_vencimento = self.dias_para_vencimento
        dto.id_plano = self.id_plano
        dto.dias_para_troca_da_dieta = self.dias_para_troca_da_dieta
        dto.descricao = self.descricao
        return dto

    def __repr__(self):
        return f"<Plano(nome='{self.descricao}')>"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
