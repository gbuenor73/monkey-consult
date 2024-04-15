from com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO
from com.monkeyconsulting.domain.dtos.valor_dto import ValorDTO
from com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel
from com.monkeyconsulting.infra.database.models.valor_model import ValorModel


class CompletoDTO:
    id_cliente = None
    id_data = None
    clientes = None
    data_pagamento = None
    inicio_dieta_treino = None
    inicio_plano = None
    ultima_troca_dieta_treino = None
    proxima_troca_dieta_treino = None
    vencimento_plano = None
    valor = None

    def to_complete(self, cliente_dto: ClienteDTO, valor_dto: ValorDTO):
        self.id_cliente = cliente_dto.id
        self.id_data = cliente_dto.data.id_data

        self.clientes = cliente_dto

        self.data_pagamento = cliente_dto.data.data_pagamento
        self.inicio_dieta_treino = cliente_dto.data.inicio_dieta_treino
        self.inicio_plano = cliente_dto.data.inicio_plano
        self.ultima_troca_dieta_treino = cliente_dto.data.ultima_troca_dieta_treino
        self.proxima_troca_dieta_treino = cliente_dto.data.proxima_troca_dieta_treino
        self.vencimento_plano = cliente_dto.data.vencimento_plano
        self.valor = valor_dto
        return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<CompletoDTO()')>"
