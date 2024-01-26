from br.com.monkeyconsulting.adapters.controllers.responses.data_resp import DataResponse
from src.br.com.monkeyconsulting.adapters.controllers.responses.dieta_treino_resp import DietaTreinoResponse
from src.br.com.monkeyconsulting.adapters.controllers.responses.plano_resp import PlanoResponse
from src.br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class ClienteResponse:

    def __init__(self, dto: ClienteDTO):
        self.nome = dto.nome
        self.telefone = dto.telefone
        self.indicador_cliente_ativo = dto.indicador_ativo
        self.id_cliente = dto.id

        if dto.plano is not None:
            self.plano = PlanoResponse(dto.plano)
            self.id_plano = dto.plano.id_plano

        if dto.dieta is not None:
            self.dieta = DietaTreinoResponse(dto.dieta)
            self.id_data = dto.data.id_data

        if dto.data is not None:
            self.data = DataResponse(dto.data)
            self.id_dieta = dto.dieta.id_dieta

    def __repr__(self):
        return f'ClienteResponse("nome:" ,{self.nome},"plano:" {self.plano},"dieta:" {self.dieta}, "data:" {self.data})'

    def to_json(self):
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'indicador_cliente_ativo': self.indicador_cliente_ativo,

            'id_plano': self.id_plano if hasattr(self, 'id_plano') else None,
            'plano': self.plano.to_json() if hasattr(self, 'plano') else None,

            'id_dieta': self.id_dieta if hasattr(self, 'id_dieta') else None,
            'dieta': self.dieta.to_json() if hasattr(self, 'dieta') else None,

            'id_data': self.id_data if hasattr(self, 'id_data') else None,
            'data': self.data.to_json() if hasattr(self, 'data') else None
        }
