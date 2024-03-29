import json

from marshmallow import Schema, fields

from br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class ClienteRequest(Schema):
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    indicador_cliente_ativo = fields.Bool(required=True)
    id_cliente = fields.Int(required=False)
    id_plano = fields.Int(required=False)
    id_dieta = fields.Int(required=False)
    id_data = fields.Int(required=False)

    def to_json(self) -> json:
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'indicador_cliente_ativo': self.indicador_cliente_ativo,
            'id_plano': self.id_plano,
            'id_dieta': self.id_dieta,
            'id_data': self.id_data
        }

    def to_dto(self):
        dto = ClienteDTO()
        dto.id = self.id_cliente
        dto.nome = self.nome
        dto.telefone = self.telefone
        dto.indicador_cliente_ativo = self.indicador_cliente_ativo
        dto.id_plano = self.id_plano
        dto.id_dieta = self.id_dieta
        dto.id_data = self.id_data
        return dto

    def from_json(self, json):
        self.nome = json.get('nome')
        self.telefone = json.get('telefone')
        self.indicador_cliente_ativo = json.get('indicador_cliente_ativo')
        self.id_cliente = json.get('id_cliente')
        self.id_plano = json.get('id_plano')
        self.id_dieta = json.get('id_dieta')
        self.id_data = json.get('id_data')
        return self

    def to_req(self, model):
        self.id_cliente = model.id_cliente
        self.nome = model.nome
        self.telefone = model.telefone
        self.indicador_cliente_ativo = model.indicador_cliente_ativo
        self.id_plano = model.id_plano
        self.id_dieta = model.id_dieta
        self.id_data = model.id_data
        return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<ClienteRequest(id='{self.id_cliente}', nome='{self.nome}')>"
