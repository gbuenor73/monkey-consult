from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class PlanoModel(Base):
    __tablename__ = 'PLANOS'

    id_plano = Column(Integer, primary_key=True)
    dias_para_vencimento = Column(Integer)
    dias_para_troca_da_dieta = Column(Integer)
    descricao = Column(String)

    # clientes = relationship("ClienteModel", backref="PLANOS")

    def to_model(self, dto):
        self.dias_para_vencimento = dto.get('dias_para_vencimento')
        self.dias_para_troca_da_dieta = dto.get('dias_para_troca_da_dieta')
        self.descricao = dto.get('descricao')
        return self

    def __repr__(self):
        return f"<Plano(nome='{self.descricao}')>"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
