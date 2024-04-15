from marshmallow import Schema, fields

from com.monkeyconsulting.domain.dtos.valor_dto import ValorDTO


class ValorRequest(Schema):
    id_valor = fields.Int(required=False)
    valor_bruto = fields.Float(required=True)
    valor_liquido = fields.Float(required=True)

    def to_json(self):
        return {
            'id_valor': self.id_valor,
            'valor_bruto': self.valor_bruto,
            'valor_liquido': self.valor_liquido
        }

    def from_json(self, json):
        self.id_valor = json.get('id_valor')
        self.valor_bruto = json.get('valor_bruto')
        self.valor_liquido = json.get('valor_liquido')
        return self

    def to_dto(self):
        dto = ValorDTO()
        dto.id_valor = self.id_valor
        dto.valor_liquido = self.valor_liquido
        dto.valor_bruto = self.valor_bruto
        return dto

    def to_request(self, dto):
        self.id_valor = dto.id_valor
        self.valor_bruto = dto.valor_bruto
        self.valor_liquido = dto.valor_liquido
        return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<ValorRequest(id='{self.id_valor}')>"
