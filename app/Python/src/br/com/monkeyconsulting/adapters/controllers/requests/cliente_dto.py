from marshmallow import Schema, fields


class ClienteDto(Schema):
    id_cliente = fields.Int(required=False)
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    indicador_cliente_ativo = fields.Int(required=True)
    id_plano = fields.Int(required=True)
    id_dieta = fields.Int(required=True)

    def to_json(self):
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'indicador_cliente_ativo': self.indicador_cliente_ativo,
            'id_plano': self.id_plano,
            'id_dieta': self.id_dieta
        }

    def to_dto(self, model):
        self.id_cliente = model.id_cliente
        self.nome = model.nome
        self.telefone = model.telefone
        self.indicador_cliente_ativo = model.indicador_cliente_ativo
        self.id_plano = model.id_plano
        self.id_dieta = model.id_dieta
        return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
