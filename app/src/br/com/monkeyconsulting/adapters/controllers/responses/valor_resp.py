from com.monkeyconsulting.domain.dtos.valor_dto import ValorDTO


class ValorResponse:
    id_valor = None
    valor_bruto = None
    valor_liquido = None

    def __init__(self, *args, **keyargs):
        super().__init__(*args, **keyargs)

    def __repr__(self):
        return f"ValorResponse(id_valor:, {self.id_valor})"

    def to_json(self):
        json = {
            'id_valor': self.id_valor if self.id_valor is not None else '',
            'valor_liquido': str(self.valor_liquido) if self.valor_liquido is not None else '',
            'valor_bruto': str(self.valor_bruto) if self.valor_bruto is not None else ''
        }

        return json

    def dto_to_response(self, dto: ValorDTO):
        if dto is not None:
            self.id_valor = dto.id_valor
            self.valor_bruto = dto.valor_bruto
            self.valor_liquido = dto.valor_liquido
        return self

