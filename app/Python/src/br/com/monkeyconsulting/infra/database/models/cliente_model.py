from br.com.monkeyconsulting.adapters.controllers.requests.cliente_req import ClienteRequest
from br.com.monkeyconsulting.infra.database.models.dietas_treinos_model import DietaTreinoModel
from br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ClienteModel(Base):
    __tablename__ = 'CLIENTES'

    id_cliente = Column(Integer, primary_key=True)
    id_plano = Column(Integer, ForeignKey(PlanoModel.id_plano), nullable=False)
    id_dieta = Column(Integer, ForeignKey(DietaTreinoModel.id_dieta), nullable=False)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    indicador_cliente_ativo = Column(Integer, nullable=False)

    plano = relationship(PlanoModel, lazy=False)
    dieta = relationship(DietaTreinoModel)

    def to_model(self, dto: ClienteRequest):
        self.nome = dto.get('nome')
        self.telefone = dto.get('telefone')
        self.indicador_cliente_ativo = dto.get('indicador_cliente_ativo')
        self.id_plano = dto.get('id_plano')
        self.id_dieta = dto.get('id_dieta')
        return self

    def __repr__(self):
        return f"<Cliente(nome='{self.nome}')>"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
