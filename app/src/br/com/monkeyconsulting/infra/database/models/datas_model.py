from datetime import datetime

from sqlalchemy import Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

from com.monkeyconsulting.domain.dtos.data_dto import DataDTO

Base = declarative_base()


class DataModel(Base):
    __tablename__ = 'DATAS'

    id_data = Column(Integer, primary_key=True)
    data_pagamento = Column(Date)
    inicio_dieta_treino = Column(Date)
    inicio_plano = Column(Date)
    ultima_troca_dieta_treino = Column(Date)
    proxima_troca_dieta_treino = Column(Date)
    vencimento_plano = Column(Date)

    def to_model(self, dto):
        self.id_data = dto.id_data
        self.data_pagamento = dto.data_pagamento
        self.inicio_dieta_treino = dto.inicio_dieta_treino
        self.inicio_plano = dto.inicio_plano
        self.ultima_troca_dieta_treino = dto.ultima_troca_dieta_treino
        self.proxima_troca_dieta_treino = dto.proxima_troca_dieta_treino
        self.vencimento_plano = dto.vencimento_plano
        return self

    def to_dto(self):
        dto = DataDTO()
        dto.id_data = self.id_data
        dto.data_pagamento = self.convert_date(self.data_pagamento)
        dto.inicio_dieta_treino = self.convert_date(self.inicio_dieta_treino)
        dto.inicio_plano = self.convert_date(self.inicio_plano)
        dto.ultima_troca_dieta_treino = self.convert_date(self.ultima_troca_dieta_treino)
        dto.proxima_troca_dieta_treino = self.convert_date(self.proxima_troca_dieta_treino)
        dto.vencimento_plano = self.convert_date(self.vencimento_plano)
        return dto

    def convert_date(self, data) -> str:
        try:
            if data is not None:
                asdd = data.strftime("%d/%m/%Y")
                return asdd
            else:
                return None
        except Exception as s:
            print(s)

    def transformar_datas(self, dto):
        if dto.data_pagamento is not None:
            self.data_pagamento = dto.data_pagamento

        if dto.inicio_dieta_treino is not None:
            self.inicio_dieta_treino = self.converte_data(dto.inicio_dieta_treino)

        if dto.inicio_plano is not None:
            self.inicio_plano = self.converte_data(dto.inicio_plano)

        if dto.ultima_troca_dieta_treino is not None:
            self.ultima_troca_dieta_treino = self.converte_data(dto.ultima_troca_dieta_treino)

        if dto.proxima_troca_dieta_treino is not None:
            self.proxima_troca_dieta_treino = (self.converte_data(dto.proxima_troca_dieta_treino))

        if dto.vencimento_plano is not None:
            self.vencimento_plano = self.converte_data(dto.vencimento_plano)

    def converte_data(self, data):
        try:
            data_convertida = datetime.strptime(data, "%d/%m/%Y")
            return data_convertida.strftime("%Y-%m-%d")
        except Exception as e:
            print(e)

    def __repr__(self):
        return f"<Data(id_data'{self.id_data}'>"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
