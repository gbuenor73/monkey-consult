import json

from marshmallow import Schema, fields

from com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class EditClienteRequest(Schema):
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    id_cliente = fields.Int(required=True)
    id_plano = fields.Int(required=True)
    id_dieta = fields.Int(required=True)
    indicador_cliente_ativo = fields.Bool(required=True)

    def to_json(self) -> json:
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'indicador_cliente_ativo': self.indicador_cliente_ativo,
            'id_plano': self.id_plano,
            'id_dieta': self.id_dieta
        }

    def to_req(self, model):
        self.id_cliente = model.id_cliente
        self.nome = model.nome
        self.telefone = model.telefone
        self.indicador_cliente_ativo = model.indicador_cliente_ativo
        self.id_plano = model.id_plano
        self.id_dieta = model.id_dieta
        return self

    def from_json(self, data_json):
        self.nome = data_json.get('nome')
        self.telefone = data_json.get('telefone')
        self.indicador_cliente_ativo = data_json.get('indicador_cliente_ativo')
        self.id_cliente = data_json.get('id_cliente')
        self.id_plano = data_json.get('id_plano')
        self.id_dieta = data_json.get('id_dieta')
        return self

    def to_dto(self):
        dto = ClienteDTO()
        dto.nome = self.nome
        dto.telefone = self.telefone
        dto.indicador_cliente_ativo = bool(self.indicador_cliente_ativo)
        dto.id = self.id_cliente

        dto.id_plano = self.id_plano
        dto.plano.id_plano = self.id_plano

        dto.id_dieta = self.id_dieta
        dto.dieta.id_dieta = self.id_dieta

        return dto

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<ClienteRequest(id='{self.id_cliente}', nome='{self.nome}')>"
