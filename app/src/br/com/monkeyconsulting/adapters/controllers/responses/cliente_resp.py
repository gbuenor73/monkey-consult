import json

from com.monkeyconsulting.adapters.controllers.responses.data_resp import DataResponse
from com.monkeyconsulting.adapters.controllers.responses.dieta_treino_resp import DietaTreinoResponse
from com.monkeyconsulting.adapters.controllers.responses.plano_resp import PlanoResponse
from com.monkeyconsulting.adapters.controllers.responses.valor_resp import ValorResponse
from com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class ClienteResponse:
    id_cliente = None
    nome = None
    telefone = None
    indicador_cliente_ativo = None
    plano = None
    dieta = None
    data = None
    valor = None

    def to_resp(self, dto: ClienteDTO):
        self.id_cliente = dto.id
        self.nome = dto.nome
        self.telefone = dto.telefone
        self.indicador_cliente_ativo = dto.indicador_cliente_ativo
        self.plano = PlanoResponse().dto_to_response(dto.plano)
        self.dieta = DietaTreinoResponse().dto_to_response(dto.dieta)
        self.data = DataResponse().dto_to_response(dto.data)
        # self.valor = ValorResponse().dto_to_response(dto.valor)
        return self

    def to_dto(self):
        dto = ClienteDTO()
        dto.id = self.id_cliente
        dto.nome = self.nome
        dto.telefone = self.telefone
        dto.indicador_cliente_ativo = self.indicador_cliente_ativo
        dto.plano.id_plano = self.plano.id_plano
        dto.dieta.id_dieta = self.dieta.id_dieta
        dto.data.id_data = self.data.id_data
        dto.valor.id_valor = self.valor.id_valor
        return dto

    def to_json(self) -> json:
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'indicador_cliente_ativo': self.indicador_cliente_ativo,
            'plano': self.plano.to_json() if hasattr(self, 'plano') else None,
            'dieta': self.dieta.to_json() if hasattr(self, 'dieta') else None,
            'data': self.data.to_json() if hasattr(self, 'data') else None,
            'valor': self.valor.to_json() if hasattr(self, 'valor') else None
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return (f'ClienteResponse("nome:" {self.nome},'
                f'"plano:" {self.plano.id_plano},'
                f'"dieta:" {self.dieta.id_dieta}, '
                f'"data:" {self.data.id_data}, '
                f'"valor:" {self.valor.id_valor})')
