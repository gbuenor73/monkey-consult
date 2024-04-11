from com.monkeyconsulting.adapters.controllers.responses.data_resp import DataResponse
from com.monkeyconsulting.adapters.controllers.responses.dieta_treino_resp import DietaTreinoResponse
from com.monkeyconsulting.adapters.controllers.responses.plano_resp import PlanoResponse
from com.monkeyconsulting.adapters.controllers.responses.valor_resp import ValorResponse
from com.monkeyconsulting.domain.dtos.completo_dto import CompletoDTO


class CompletoResponse:
    id_cliente = None
    nome = None
    telefone = None
    indicador_cliente_ativo = None
    plano = PlanoResponse()
    dieta = DietaTreinoResponse()
    data = DataResponse()
    valor = ValorResponse()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def __init__(self, dto: ClienteDTO):
    #     self.id_cliente = dto.id
    #     self.nome = dto.nome
    #     self.telefone = dto.telefone
    #     self.indicador_cliente_ativo = dto.indicador_cliente_ativo
    #
    #     self.plano = PlanoResponse(dto.plano) if dto.plano is not None else None
    #     self.dieta = DietaTreinoResponse(dto.dieta) if dto.dieta is not None else None
    #
    #     if dto.data is not None:
    #         self.data = DataResponse(dto.data)
    #         self.data_pagamento = dto.data.data_pagamento
    #         self.inicio_dieta_treino = dto.data.inicio_dieta_treino
    #         self.ultima_troca_dieta_treino = dto.data.ultima_troca_dieta_treino
    #         self.proxima_troca_dieta_treino = dto.data.proxima_troca_dieta_treino
    #         self.vencimento_plano = dto.data.vencimento_plano
    #     else:
    #         self.data = None

    def __repr__(self):
        return f'CompletoResponse("id_cliente:" ,{self.id_cliente},"data_pagamento:" {self.data_pagamento})'

    def to_json(self):
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'indicador_cliente_ativo': self.indicador_cliente_ativo,
            'dieta': self.dieta.to_json() if self.dieta is not None else {},
            'plano': self.plano.to_json() if self.plano is not None else {},
            'data': self.data.to_json() if self.data is not None else {},
            'valor': self.valor.to_json() if self.valor is not None else {}
        }

    def dto_to_response(self, dto: CompletoDTO):

        if dto is not None:
            self.id_cliente = dto.id
            self.nome = dto.nome
            self.telefone = dto.telefone
            self.indicador_cliente_ativo = dto.indicador_cliente_ativo
            self.plano = PlanoResponse().dto_to_response(dto.plano) \
                if dto.plano is not None else None
            self.dieta = DietaTreinoResponse().dto_to_response(dto.dieta) \
                if dto.dieta is not None else None

            if dto.data is not None:
                self.data = DataResponse().dto_to_response(dto.data)

            if dto.valor is not None:
                self.valor = ValorResponse().dto_to_response(dto.valor)
        return self
