from datetime import datetime

from src.br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO


class DataResponse:
    id_data = None
    data_pagamento = None
    inicio_dieta_treino = None
    ultima_troca_dieta_treino = None
    proxima_troca_dieta_treino = None
    vencimento_plano = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'DataResponse("id_data:" ,{self.id_data},"data_pagamento:" {self.data_pagamento})'

    def to_json(self):
        return {
            'id_data': self.id_data if self.id_data is not None else '',
            'data_pagamento': self.data_pagamento if self.data_pagamento is not None else '',
            'inicio_dieta_treino': self.inicio_dieta_treino if self.inicio_dieta_treino is not None else '',
            'ultima_troca_dieta_treino': self.ultima_troca_dieta_treino if self.ultima_troca_dieta_treino is not None else '',
            'proxima_troca_dieta_treino': self.proxima_troca_dieta_treino if self.proxima_troca_dieta_treino is not None else '',
            'vencimento_plano': self.vencimento_plano if self.vencimento_plano is not None else ''
        }

    def dto_to_response(self, dto: DataDTO):
        if dto is not None:
            self.id_data = dto.id_data
            self.data_pagamento = dto.data_pagamento
            self.inicio_dieta_treino = dto.inicio_dieta_treino
            self.ultima_troca_dieta_treino = dto.ultima_troca_dieta_treino
            self.proxima_troca_dieta_treino = dto.proxima_troca_dieta_treino
            self.vencimento_plano = dto.vencimento_plano
        return self

    def transformar_datas(self):
        retorno = self
        if self.data_pagamento is not None:
            retorno.data_pagamento = self.converte_data(self.data_pagamento)

        if self.inicio_dieta_treino is not None:
            retorno.inicio_dieta_treino = self.converte_data(self.inicio_dieta_treino)

        if self.ultima_troca_dieta_treino is not None:
            retorno.ultima_troca_dieta_treino = self.converte_data(self.ultima_troca_dieta_treino)

        if self.proxima_troca_dieta_treino is not None:
            retorno.proxima_troca_dieta_treino = (
                self.converte_data(self.proxima_troca_dieta_treino))

        if self.vencimento_plano is not None:
            retorno.vencimento_plano = self.converte_data(self.vencimento_plano)

        return retorno

    def converte_data(self, data):
        data_convertida = datetime.strptime(data, "%d/%m/%Y")
        return data_convertida.strftime("%Y-%m-%d")
