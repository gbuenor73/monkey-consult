from src.br.com.monkeyconsulting.infra.database.models.dietas_treinos_model import DietaTreinoModel


class DietaTreinoDTO:
    id_dieta = None
    descricao = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<DietaTreinoDTO(id_dieta='{self.id_dieta}')>"

    def to_dto(self, dieta: DietaTreinoModel):
        self.id_dieta = dieta.id_dieta
        self.descricao = dieta.descricao
        return self
