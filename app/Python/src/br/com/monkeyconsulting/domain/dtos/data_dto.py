class DataDTO:

    def __init__(self, id_data, data_pagamento, inicio_dieta_treino, ultima_troca_dieta_treino,
                 proxima_troca_dieta_treino, vencimento_plano):
        self.id_data = id_data
        self.data_pagamento = data_pagamento
        self.inicio_dieta_treino = inicio_dieta_treino
        self.ultima_troca_dieta_treino = ultima_troca_dieta_treino
        self.proxima_troca_dieta_treino = proxima_troca_dieta_treino
        self.vencimento_plano = vencimento_plano

    @staticmethod
    def to_dto(model):
        if model is not None:
            return DataDTO(
                model.id_data,
                model.data_pagamento,
                model.inicio_dieta_treino,
                model.ultima_troca_dieta_treino,
                model.proxima_troca_dieta_treino,
                model.vencimento_plano
            )
        else:
            return DataDTO(
                None,
                None,
                None,
                None,
                None,
                None
            )
