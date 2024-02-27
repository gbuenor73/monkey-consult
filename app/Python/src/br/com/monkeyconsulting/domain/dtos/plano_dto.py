class PlanoDTO:
    id_plano = None
    dias_para_vencimento = None
    dias_para_troca_da_dieta = None
    descricao = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<PlanoDTO(id_plano='{self.id_plano}')>"

    def set_id(self, id_plano):
        self.id_plano = id_plano
        return self
