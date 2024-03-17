from datetime import datetime

from marshmallow import Schema, fields

from br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO


class DataRequest(Schema):
    id_data = fields.Int(required=False)
    iniciar_plano_check = fields.Bool(required=False)
    mesma_data_check = fields.Bool(required=False)
    data_pagamento = fields.Date(required=False)
    inicio_dieta_treino = fields.Date(required=False)
    ultima_troca_dieta_treino = fields.Date(required=False)
    proxima_troca_dieta_treino = fields.Date(required=False)
    vencimento_plano = fields.Date(required=False)
    inicio_plano = fields.Date(required=False)

    def to_json(self):
        return {
            'id_data': self.id_data,
            'mesma_data_check': self.mesma_data_check,
            'iniciar_plano_check': self.iniciar_plano_check,
            'data_pagamento': self.data_pagamento,
            'inicio_dieta_treino': self.inicio_dieta_treino,
            'ultima_troca_dieta_treino': self.ultima_troca_dieta_treino,
            'proxima_troca_dieta_treino': self.proxima_troca_dieta_treino,
            'vencimento_plano': self.vencimento_plano,
            'inicio_plano': self.inicio_plano,
        }

    def to_dto(self):
        try:
            dto = DataDTO()
            if hasattr(self, 'id_data'):
                dto.id_data = self.id_data

            if hasattr(self, 'iniciar_plano_check'):
                dto.iniciar_plano_check = self.iniciar_plano_check

            if hasattr(self, 'mesma_data_check'):
                dto.mesma_data_check = self.mesma_data_check

            if hasattr(self, 'data_pagamento'):
                dto.data_pagamento = datetime.strptime(self.data_pagamento, '%Y-%m-%d').date() \
                    if self.data_pagamento is not None else None

            if hasattr(self, 'inicio_dieta_treino'):
                dto.inicio_dieta_treino = datetime.strptime(self.inicio_dieta_treino, '%Y-%m-%d').date() \
                    if self.inicio_dieta_treino is not None else None

            if hasattr(self, 'inicio_plano'):
                dto.inicio_plano = datetime.strptime(self.inicio_plano, '%Y-%m-%d').date() \
                    if self.inicio_plano is not None else None

            if hasattr(self, 'ultima_troca_dieta_treino'):
                dto.ultima_troca_dieta_treino = datetime.strptime(self.ultima_troca_dieta_treino, '%Y-%m-%d').date() \
                    if self.ultima_troca_dieta_treino is not None else None

            if hasattr(self, 'proxima_troca_dieta_treino'):
                dto.proxima_troca_dieta_treino = datetime.strptime(self.proxima_troca_dieta_treino, '%Y-%m-%d').date() \
                    if self.proxima_troca_dieta_treino is not None else None

            if hasattr(self, 'vencimento_plano'):
                dto.vencimento_plano = datetime.strptime(self.vencimento_plano, '%Y-%m-%d').date() \
                    if self.vencimento_plano is not None else None

            return dto

        except Exception as e:
            print(e)

    def to_request(self, model):
        self.id_data = model.id_data
        self.data_pagamento = model.data_pagamento
        self.inicio_dieta_treino = model.inicio_dieta_treino
        self.inicio_plano = model.inicio_plano
        self.ultima_troca_dieta_treino = model.ultima_troca_dieta_treino
        self.proxima_troca_dieta_treino = model.proxima_troca_dieta_treino
        self.vencimento_plano = model.vencimento_plano
        return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<DataRequest(id='{self.id_data}', data_pagamento='{self.data_pagamento}')>"
