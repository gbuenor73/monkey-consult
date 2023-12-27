from app.Python.src.br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO


class DataResponse:

    def __init__(self, dto: DataDTO):
        self.id_data = dto.id_data
        self.id_cliente = dto.id_cliente
        self.data_pagamento = dto.data_pagamento
        self.inicio_dieta_treino = dto.inicio_dieta_treino
        self.ultima_troca_dieta_treino = dto.ultima_troca_dieta_treino
        self.proxima_troca_dieta_treino = dto.proxima_troca_dieta_treino
        self.vencimento_plano = dto.vencimento_plano

    def __repr__(self):
        return f'DataResponse("id_data:" ,{self.id_data},"id_cliente:" {self.id_cliente},"data_pagamento:" {self.data_pagamento})'

    def to_json(self):
        return {
            'id_data': self.id_data,
            'id_cliente': self.id_cliente,
            'data_pagamento': self.data_pagamento,
            'inicio_dieta_treino': self.inicio_dieta_treino,
            'ultima_troca_dieta_treino': self.ultima_troca_dieta_treino,
            'proxima_troca_dieta_treino': self.proxima_troca_dieta_treino,
            'vencimento_plano': self.vencimento_plano
        }
