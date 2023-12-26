from br.com.monkeyconsulting.adapters.controllers.responses.response_completo_resp import ResponseCompletoResponse
from br.com.monkeyconsulting.domain.utils.utils import list_to_json, format_response
from br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository
from br.com.monkeyconsulting.infra.database.repositories.datas_repository import DatasRepository
from br.com.monkeyconsulting.infra.database.repositories.dieta_repository import DietasRepository
from br.com.monkeyconsulting.infra.database.repositories.planos_repository import PlanosRepository


class NegocioService:

    def __init__(self):
        self.clientes_repo = ClientesRepository()
        self.datas_repo = DatasRepository()
        self.planos_repo = PlanosRepository()
        self.dietas_repo = DietasRepository()

    def obtem_todos_dados(self) -> ResponseCompletoResponse:
        clientes = self.clientes_repo.busca_todos_clientes()
        cliente = clientes[0]
        return ResponseCompletoResponse(cliente, None, None, None, None, None)


    def post(self):
        return "teste"
