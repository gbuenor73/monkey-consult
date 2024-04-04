from com.monkeyconsulting.infra.database.repositories.completo_repository import CompletoRepository
from com.monkeyconsulting.adapters.controllers.responses.completo_resp import CompletoResponse


class NegocioService:

    def __init__(self):
        self.repo = CompletoRepository()

    def obtem_todos_dados(self):
        completo_dto = self.repo.busca_completa()

        return [CompletoResponse().dto_to_response(dto) for dto in completo_dto]
