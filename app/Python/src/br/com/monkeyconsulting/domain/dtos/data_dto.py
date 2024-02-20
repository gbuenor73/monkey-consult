from _datetime import date

from br.com.monkeyconsulting.infra.database.models.datas_model import DataModel


class DataDTO:
    id_data = None
    data_pagamento = None
    inicio_dieta_treino = None
    ultima_troca_dieta_treino = None
    proxima_troca_dieta_treino = None
    vencimento_plano = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<DataDTO(id_data='{self.id_data}')>"

    def to_dto(self, model: DataModel):
        if model is None:
            return DataDTO()

        self.id_data = model.id_data
        self.data_pagamento = self.convert_date(model.data_pagamento)
        self.inicio_dieta_treino = self.convert_date(model.inicio_dieta_treino)
        self.ultima_troca_dieta_treino = self.convert_date(model.ultima_troca_dieta_treino)
        self.proxima_troca_dieta_treino = self.convert_date(model.proxima_troca_dieta_treino)
        self.vencimento_plano = self.convert_date(model.vencimento_plano)
        return self

    def convert_date(self, data) -> str:
        if data is not None:
            return date.strftime(data, "%d/%m/%Y")
        return data
