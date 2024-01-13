from src.br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class CompletoDTO:

    def __init__(self, id_data, id_cliente, clientes, data_pagamento, inicio_dieta_treino, ultima_troca_dieta_treino,
                 proxima_troca_dieta_treino, vencimento_plano):
        self.id_data = id_data
        self.id_cliente = id_cliente
        self.clientes = ClienteDTO.to_dto(clientes)
        self.data_pagamento = data_pagamento
        self.inicio_dieta_treino = inicio_dieta_treino
        self.ultima_troca_dieta_treino = ultima_troca_dieta_treino
        self.proxima_troca_dieta_treino = proxima_troca_dieta_treino
        self.vencimento_plano = vencimento_plano

    @staticmethod
    def to_dto(model):
        return CompletoDTO(
            model.id_data,
            model.id_cliente,
            model.clientes,
            model.data_pagamento,
            model.inicio_dieta_treino,
            model.ultima_troca_dieta_treino,
            model.proxima_troca_dieta_treino,
            model.vencimento_plano
        )
