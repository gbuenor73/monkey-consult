from br.com.monkeyconsulting.adapters.controllers.responses.data_resp import DataResponse
from br.com.monkeyconsulting.adapters.controllers.responses.dieta_treino_resp import DietaTreinoResponse
from br.com.monkeyconsulting.adapters.controllers.responses.plano_resp import PlanoResponse
from br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class CompletoResponse:

    def __init__(self, dto: ClienteDTO):
        self.id_cliente = dto.id
        self.plano = PlanoResponse(dto.plano)
        self.dieta = DietaTreinoResponse(dto.dieta)
        self.data = DataResponse(dto.data)
        self.nome = dto.nome
        self.telefone = dto.telefone
        self.data_pagamento = dto.data.data_pagamento
        self.inicio_dieta_treino = dto.data.inicio_dieta_treino
        self.ultima_troca_dieta_treino = dto.data.ultima_troca_dieta_treino
        self.proxima_troca_dieta_treino = dto.data.proxima_troca_dieta_treino
        self.vencimento_plano = dto.data.vencimento_plano

    def __repr__(self):
        return f'CompletoResponse("id_cliente:" ,{self.id_cliente},"data_pagamento:" {self.data_pagamento})'

    def to_json(self):
        if self.data_pagamento is None:
            data_pagamento = ''
        else:
            data_pagamento = self.data_pagamento

        if self.inicio_dieta_treino is None:
            inicio_dieta_treino = ''
        else:
            inicio_dieta_treino = self.inicio_dieta_treino

        if self.ultima_troca_dieta_treino is None:
            ultima_troca_dieta_treino = ''
        else:
            ultima_troca_dieta_treino = self.ultima_troca_dieta_treino

        if self.proxima_troca_dieta_treino is None:
            proxima_troca_dieta_treino = ''
        else:
            proxima_troca_dieta_treino = self.proxima_troca_dieta_treino

        if self.vencimento_plano is None:
            vencimento_plano = ''
        else:
            vencimento_plano = self.vencimento_plano

        return {
            'id_cliente': self.id_cliente,
            'plano': self.plano.to_json(),
            'nome': self.nome,
            'telefone': self.telefone,
            'dieta': self.dieta.to_json(),
            'data_pagamento': data_pagamento,
            'inicio_dieta_treino': inicio_dieta_treino,
            'ultima_troca_dieta_treino': ultima_troca_dieta_treino,
            'proxima_troca_dieta_treino': proxima_troca_dieta_treino,
            'vencimento_plano': vencimento_plano
        }
