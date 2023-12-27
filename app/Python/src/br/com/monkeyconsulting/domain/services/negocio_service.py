from app.Python.src.br.com.monkeyconsulting.adapters.controllers.responses.completo_resp import \
    CompletoResponse
from app.Python.src.br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository
from app.Python.src.br.com.monkeyconsulting.infra.database.repositories.datas_repository import DatasRepository
from app.Python.src.br.com.monkeyconsulting.infra.database.repositories.dieta_repository import DietasRepository
from app.Python.src.br.com.monkeyconsulting.infra.database.repositories.planos_repository import PlanosRepository


class NegocioService:

    def __init__(self):
        self.clientes_repo = ClientesRepository()
        self.datas_repo = DatasRepository()
        self.planos_repo = PlanosRepository()
        self.dietas_repo = DietasRepository()

    def obtem_todos_dados(self):
        completo_responses = self.datas_repo.retorno_completo()
        return [CompletoResponse(completo_response) for completo_response in completo_responses]
