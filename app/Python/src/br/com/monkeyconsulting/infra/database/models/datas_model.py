from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DatasModel(Base):
    __tablename__ = 'DATAS'

    id_datas = Column(Integer)
    id_cliente = Column(Integer)
    data_pagamento = Column(String)
    inicio_dieta_treino = Column(String)
    ultima_troca_dieta_treino = Column(String)
    proxima_troca_dieta_treino = Column(String)
    vencimento_plano = Column(String)

    def __repr__(self):
        return f"<Data(id_data'{self.id_datas}'>"

    def to_model(self, dto):
        self.id_cliente = dto.get('id_cliente')
        self.data_pagamento = dto.get('data_pagamento')
        self.inicio_dieta_treino = dto.get('inicio_dieta_treino')
        self.ultima_troca_dieta_treino = dto.get('ultima_troca_dieta_treino')
        self.proxima_troca_dieta_treino = dto.get('proxima_troca_dieta_treino')
        self.vencimento_plano = dto.get('vencimento_plano')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
