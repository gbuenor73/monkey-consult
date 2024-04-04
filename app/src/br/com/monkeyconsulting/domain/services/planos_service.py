from com.monkeyconsulting.adapters.controllers.responses.plano_resp import PlanoResponse
from com.monkeyconsulting.infra.database.repositories.planos_repository import PlanosRepository


class PlanosService:

    def __init__(self):
        self.repo = PlanosRepository()

    def busca_todos_planos(self):
        planos = self.repo.busca_todos_planos()
        return planos

    def busca_plano_por_id(self, id):
        plano = self.repo.busca_plano_por_id(id)
        return plano

    def insere_plano(self, dto):
        dto_response = self.repo.insere_plano(dto)
        return PlanoResponse(dto_response)
