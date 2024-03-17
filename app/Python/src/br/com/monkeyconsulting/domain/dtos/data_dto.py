class DataDTO:
    id_data = None
    data_pagamento = None
    inicio_dieta_treino = None
    inicio_plano = None
    iniciar_plano_check = None
    mesma_data_check = None
    ultima_troca_dieta_treino = None
    proxima_troca_dieta_treino = None
    vencimento_plano = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<DataDTO(id_data='{self.id_data}')>"

