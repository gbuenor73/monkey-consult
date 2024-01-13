import json

from marshmallow import Schema, fields


class ClienteRequest(Schema):
    id_cliente = fields.Int(required=False)
    id_plano = fields.Int(required=False)
    id_dieta = fields.Int(required=False)
    id_data = fields.Int(required=False)
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    indicador_cliente_ativo = fields.Int(required=True)

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
