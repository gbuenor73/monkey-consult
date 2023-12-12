from marshmallow import Schema, fields


class DietasDto(Schema):
    id_dieta = fields.Int(required=False)
    descricao = fields.Str(required=True)

    def to_json(self):
        return {
            'id_dieta': self.id_dieta,
            'descricao': self.descricao
        }

    def to_dto(self, model):
        self.id_dieta = model.id_dieta
        self.descricao = model.descricao
        return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
