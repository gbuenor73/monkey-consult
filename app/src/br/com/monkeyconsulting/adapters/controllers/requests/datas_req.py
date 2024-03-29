from marshmallow import Schema, fields


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
