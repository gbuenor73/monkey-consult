from src.br.com.monkeyconsulting.infra.database.models.dietas_treinos_model import DietaTreinoModel


class DietaTreinoDTO:
    def __init__(self, id_dieta, descricao):
        self.id_dieta = id_dieta
        self.descricao = descricao

    @staticmethod
    def to_dto(dieta: DietaTreinoModel):
        DietaTreinoDTO.id_dieta = dieta.id_dieta
        DietaTreinoDTO.descricao = dieta.descricao
        return DietaTreinoDTO
