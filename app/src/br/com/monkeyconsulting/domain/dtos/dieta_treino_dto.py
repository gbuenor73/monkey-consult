class DietaTreinoDTO:
    id_dieta = None
    descricao = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<DietaTreinoDTO(id_dieta='{self.id_dieta}')>"
