import json

from br.com.monkeyconsulting.adapters.controllers.responses.data_resp import DataResponse
from br.com.monkeyconsulting.adapters.controllers.responses.dieta_treino_resp import DietaTreinoResponse
from br.com.monkeyconsulting.adapters.controllers.responses.plano_resp import PlanoResponse
from src.br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class ClienteResponse:
    id_cliente = None
    nome = None
    telefone = None
    indicador_cliente_ativo = None
    plano = None
    dieta = None
    data = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'ClienteResponse("nome:" ,{self.nome},"plano:" {self.plano},"dieta:" {self.dieta}, "data:" {self.data})'

    def to_json(self) -> json:
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'indicador_cliente_ativo': self.indicador_cliente_ativo,
            'plano': self.plano.to_json() if hasattr(self, 'plano') else None,
            'dieta': self.dieta.to_json() if hasattr(self, 'dieta') else None,
            'data': self.data.to_json() if hasattr(self, 'data') else None
        }

    def dto_to_resp(self, dto: ClienteDTO):
        self.id_cliente = dto.id
        self.nome = dto.nome
        self.telefone = dto.telefone
        self.indicador_cliente_ativo = dto.indicador_cliente_ativo
        self.plano = PlanoResponse().dto_to_response(dto.plano)
        self.dieta = DietaTreinoResponse().dto_to_response(dto.dieta)
        self.data = DataResponse().dto_to_response(dto.data)

        return self
