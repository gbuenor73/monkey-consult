from decimal import Decimal

from sqlalchemy import Column, Integer, DECIMAL
from sqlalchemy.orm import declarative_base

from com.monkeyconsulting.domain.dtos.valor_dto import ValorDTO

Base = declarative_base()


class ValorModel(Base):
    __tablename__ = 'VALORES'

    id_valor = Column(Integer, primary_key=True)
    valor_bruto = Column(DECIMAL(precision=10, scale=2))
    valor_liquido = Column(DECIMAL(precision=10, scale=2))

    def to_model(self, dto):
        self.id_valor = dto.id_valor
        self.valor_bruto = dto.valor_bruto
        self.valor_liquido = dto.valor_liquido
        return self

    def to_dto(self):
        dto = ValorDTO()
        dto.id_valor = self.id_valor
        dto.valor_bruto = Decimal(str(self.valor_bruto))
        dto.valor_liquido = Decimal(str(self.valor_liquido))
        return dto
