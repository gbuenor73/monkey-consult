from br.com.monkeyconsulting.adapters.controllers.responses.data_resp import DataResponse
from src.br.com.monkeyconsulting.adapters.controllers.responses.dieta_treino_resp import DietaTreinoResponse
from src.br.com.monkeyconsulting.adapters.controllers.responses.plano_resp import PlanoResponse
from src.br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class ClienteResponse:

    def __init__(self, dto: ClienteDTO):
        self.id_cliente = dto.id
        self.id_plano = dto.plano.id_plano
        self.id_dieta = dto.dieta.id_dieta
        self.id_data = dto.data.id_data
        self.nome = dto.nome
        self.telefone = dto.telefone
        self.indicador_cliente_ativo = dto.indicador_ativo
        self.plano = PlanoResponse(dto.plano)
        self.dieta = DietaTreinoResponse(dto.dieta)
        self.data = DataResponse(dto.data)

    def __repr__(self):
        return f'ClienteResponse("nome:" ,{self.nome},"plano:" {self.plano},"dieta:" {self.dieta}, "data:" {self.data})'

    # @staticmethod
    def to_json(self):
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'indicador_cliente_ativo': self.indicador_cliente_ativo,
            'id_plano': self.id_plano,
            'id_dieta': self.id_dieta,
            'id_data': self.id_data,
            'plano': self.plano.to_json(),
            'dieta': self.dieta.to_json(),
            'data': self.data.to_json()
        }
