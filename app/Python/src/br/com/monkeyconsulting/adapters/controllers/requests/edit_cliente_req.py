import json

from marshmallow import Schema, fields


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<ClienteRequest(id='{self.id_cliente}', nome='{self.nome}')>"
