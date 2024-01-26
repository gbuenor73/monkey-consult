from br.com.monkeyconsulting.adapters.controllers.responses.data_resp import DataResponse
from br.com.monkeyconsulting.adapters.controllers.responses.dieta_treino_resp import DietaTreinoResponse
from br.com.monkeyconsulting.adapters.controllers.responses.plano_resp import PlanoResponse
from br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class CompletoResponse:

    def __init__(self, dto: ClienteDTO):
        self.id_cliente = dto.id
        self.nome = dto.nome
        self.telefone = dto.telefone

        self.plano = PlanoResponse(dto.plano) if dto.plano is not None else None
        self.dieta = DietaTreinoResponse(dto.dieta) if dto.dieta is not None else None

        if dto.data is not None:
            self.data = DataResponse(dto.data)
            self.data_pagamento = dto.data.data_pagamento
            self.inicio_dieta_treino = dto.data.inicio_dieta_treino
            self.ultima_troca_dieta_treino = dto.data.ultima_troca_dieta_treino
            self.proxima_troca_dieta_treino = dto.data.proxima_troca_dieta_treino
            self.vencimento_plano = dto.data.vencimento_plano
        else:
            self.data = None

    def __repr__(self):
        return f'CompletoResponse("id_cliente:" ,{self.id_cliente},"data_pagamento:" {self.data_pagamento})'

    def to_json(self):
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'dieta': self.dieta.to_json() if self.dieta is not None else {},
            'plano': self.plano.to_json() if self.plano is not None else {},
            'data': self.data.to_json() if self.data is not None else {}
        }
