from br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel


class CompletoDTO:
    id_data = None
    id_cliente = None
    clientes = None
    data_pagamento = None
    inicio_dieta_treino = None
    iniciar_plano = None
    ultima_troca_dieta_treino = None
    proxima_troca_dieta_treino = None
    vencimento_plano = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<CompletoDTO()')>"

