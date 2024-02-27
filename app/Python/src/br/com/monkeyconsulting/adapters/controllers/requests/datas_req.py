from marshmallow import Schema, fields

from br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO


class DataRequest(Schema):
    id_data = fields.Int(required=False)
    data_pagamento = fields.Date(required=False)
    inicio_dieta_treino = fields.Date(required=False)
    ultima_troca_dieta_treino = fields.Date(required=False)
    proxima_troca_dieta_treino = fields.Date(required=False)
    vencimento_plano = fields.Date(required=False)

    def to_json(self):
        return {
            'id_data': self.id_data,
            'data_pagamento': self.data_pagamento,
            'inicio_dieta_treino': self.inicio_dieta_treino,
            'ultima_troca_dieta_treino': self.ultima_troca_dieta_treino,
            'proxima_troca_dieta_treino': self.proxima_troca_dieta_treino,
            'vencimento_plano': self.vencimento_plano
        }

    def to_dto(self):
        dto = DataDTO()

        try:

            if hasattr(self, 'id_data'):
                dto.id_data = self.id_data

            if hasattr(self, 'data_pagamento'):
                dto.data_pagamento =  self.data_pagamento

            if hasattr(self, 'inicio_dieta_treino'):
                dto.inicio_dieta_treino = self.inicio_dieta_treino

            if hasattr(self, 'ultima_troca_dieta_treino'):
                dto.ultima_troca_dieta_treino = self.ultima_troca_dieta_treino

            if hasattr(self, 'vencimento_plano'):
                dto.vencimento_plano = self.vencimento_plano

            # dto.id_data = self.id_data if hasattr(self, 'id_data') is not None else None
            # dto.data_pagamento = self.data_pagamento
            # dto.inicio_dieta_treino = self.inicio_dieta_treino
            # dto.ultima_troca_dieta_treino = self.ultima_troca_dieta_treino
            # dto.proxima_troca_dieta_treino = self.proxima_troca_dieta_treino
            # dto.vencimento_plano = self.vencimento_plano
        except Exception as e:
            print(e)

        return dto

    def to_request(self, model):
        self.id_data = model.id_data
        self.data_pagamento = model.data_pagamento
        self.inicio_dieta_treino = model.inicio_dieta_treino
        self.ultima_troca_dieta_treino = model.ultima_troca_dieta_treino
        self.proxima_troca_dieta_treino = model.proxima_troca_dieta_treino
        self.vencimento_plano = model.vencimento_plano
        return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<DataRequest(id='{self.id_data}', inicio_dieta_treino='{self.inicio_dieta_treino}')>"
