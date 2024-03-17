from marshmallow import Schema, fields


class PlanoRequest(Schema):
    id_plano = fields.Int(required=False)
    dias_para_vencimento = fields.Int(required=True)
    dias_para_troca_da_dieta = fields.Int(required=True)
    descricao = fields.Str(required=True)

    def to_json(self):
        return {
            'id_plano': self.id_plano,
            'dias_para_vencimento': self.dias_para_vencimento,
            'dias_para_troca_da_dieta': self.dias_para_troca_da_dieta,
            'descricao': self.descricao
        }

    def to_request(self, dto):
        self.id_plano = dto.id_plano
        self.dias_para_vencimento = dto.dias_para_vencimento
        self.dias_para_troca_da_dieta = dto.dias_para_troca_da_dieta
        self.descricao = dto.descricao
        return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<PlanoRequest(id='{self.id_plano}', dias_para_vencimento='{self.dias_para_vencimento}')>"
