class ValorDTO:
    id_valor = None
    valor_bruto = None
    valor_liquido = None

    def __init__(self, *args, **keyargs):
        super().__init__(*args, **keyargs)

    def __repr__(self):
        return f"<ValorDTO(id_valor='{self.id_valor}'>"
