from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel

Base = declarative_base()


class DataModel(Base):
    __tablename__ = 'DATAS'

    id_data = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey(ClienteModel.id_cliente), nullable=False)
    data_pagamento = Column(Date)
    inicio_dieta_treino = Column(Date)
    ultima_troca_dieta_treino = Column(Date)
    proxima_troca_dieta_treino = Column(Date)
    vencimento_plano = Column(Date)

    clientes = relationship(ClienteModel)

    def to_model(self, dto):
        self.id_cliente = dto.get('id_cliente')
        self.data_pagamento = dto.get('data_pagamento')
        self.inicio_dieta_treino = dto.get('inicio_dieta_treino')
        self.ultima_troca_dieta_treino = dto.get('ultima_troca_dieta_treino')
        self.proxima_troca_dieta_treino = dto.get('proxima_troca_dieta_treino')
        self.vencimento_plano = dto.get('vencimento_plano')
        return self

    def __repr__(self):
        return f"<Data(id_data'{self.id_data}'>"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
