from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ClienteModel(Base):
    __tablename__ = 'CLIENTES'

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String)
    telefone = Column(String)
    indicador_cliente_ativo = Column(Integer)
    id_plano = Column(Integer)
    id_dieta = Column(Integer)

    def __repr__(self):
        return f"<Cliente(nome='{self.nome}')>"

    def to_model(self, dto):
        self.nome = dto.get('nome')
        self.telefone = dto.get('telefone')
        self.indicador_cliente_ativo = dto.get('indicador_cliente_ativo')
        self.id_plano = dto.get('id_plano')
        self.id_dieta = dto.get('id_dieta')
        return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
