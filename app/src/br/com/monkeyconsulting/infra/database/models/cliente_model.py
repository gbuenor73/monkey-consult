from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO
from br.com.monkeyconsulting.infra.database.models.datas_model import DataModel
from src.br.com.monkeyconsulting.infra.database.models.dietas_treinos_model import DietaTreinoModel
from src.br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel

Base = declarative_base()


class ClienteModel(Base):
    __tablename__ = 'CLIENTES'

    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    indicador_cliente_ativo = Column(Boolean, nullable=False)

    id_cliente = Column(Integer, primary_key=True)
    id_plano = Column(Integer, ForeignKey(PlanoModel.id_plano), nullable=False)
    id_dieta = Column(Integer, ForeignKey(DietaTreinoModel.id_dieta), nullable=False)
    id_data = Column(Integer, ForeignKey(DataModel.id_data), nullable=False)

    plano = relationship(PlanoModel, lazy=False)
    dieta = relationship(DietaTreinoModel)
    data = relationship(DataModel)

    def to_model(self, dto: ClienteDTO) -> 'ClienteModel':
        self.id_cliente = dto.id
        self.nome = dto.nome
        self.telefone = dto.telefone
        self.indicador_cliente_ativo = dto.indicador_cliente_ativo
        self.id_plano = dto.plano.id_plano if dto.plano is not None else None
        self.id_dieta = dto.dieta.id_dieta if dto.dieta is not None else None
        self.id_data = dto.data.id_data if dto.data is not None else None
        return self

    def to_dto(self):
        dto = ClienteDTO()
        dto.id = self.id_cliente
        dto.nome = self.nome
        dto.telefone = self.telefone
        dto.indicador_cliente_ativo = self.indicador_cliente_ativo
        dto.plano = self.plano.to_dto() if self.plano is not None else None
        dto.dieta = self.dieta.to_dto() if self.dieta is not None else None
        dto.data = self.data.to_dto() if self.data is not None else None
        return dto

    def __repr__(self):
        return f"<ClienteModel(id='{self.id_cliente}')>"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
