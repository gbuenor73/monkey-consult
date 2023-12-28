from src.br.com.monkeyconsulting.adapters.controllers.responses.dieta_treino_resp import DietaTreinoResponse
from src.br.com.monkeyconsulting.infra.database.repositories.dieta_repository import DietasRepository


class DietaTreinoService:

    def __init__(self):
        self.repo = DietasRepository()

    def busca_todas_dietas(self):
        dietas = self.repo.busca_todas_dietas()
        return [DietaTreinoResponse(dieta) for dieta in dietas]

    def busca_dieta_por_id(self, id_dieta):
        dieta_dto = self.repo.busca_dietas_por_id(id_dieta)
        return DietaTreinoResponse(dieta_dto)

    def insere_dieta(self, dto):
        dto_response = self.repo.insere_dieta(dto)
        return DietaTreinoResponse(dto_response)
