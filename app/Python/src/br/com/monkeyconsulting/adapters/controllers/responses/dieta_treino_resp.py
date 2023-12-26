import json

from br.com.monkeyconsulting.domain.dtos.dieta_treino_dto import DietaTreinoDTO


class DietaTreinoResponse:
    def __init__(self, dto: DietaTreinoDTO):
        self.id_dieta = dto.id_dieta
        self.descricao = dto.descricao

    def __repr__(self):
        return f"""
            id_dieta: {self.id_dieta},
            descricao: {self.descricao}
        """

    def to_json(self) -> json:
        return {
            'id_dieta': self.id_dieta,
            'descricao': self.descricao
        }
