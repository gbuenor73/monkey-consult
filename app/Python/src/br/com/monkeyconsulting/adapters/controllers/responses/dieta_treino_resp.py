import json

from src.br.com.monkeyconsulting.domain.dtos.dieta_treino_dto import DietaTreinoDTO


class DietaTreinoResponse:
    id_dieta = None
    descricao = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"""
            id_dieta: {self.id_dieta},
            descricao: {self.descricao}
        """

    def to_json(self) -> json:
        return {
            'id_dieta': self.id_dieta if self.id_dieta is not None else '',
            'descricao': self.descricao if self.descricao is not None else ''
        }

    def dto_to_response(self, dto: DietaTreinoDTO):
        if dto is not None:
            self.id_dieta = dto.id_dieta
            self.descricao = dto.descricao
        return self
