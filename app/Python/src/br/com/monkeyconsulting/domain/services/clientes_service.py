from br.com.monkeyconsulting.adapters.controllers.responses.clientes_resp import ClienteResponse
from br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository


class ClientesService:

    def __init__(self):
        self.repo = ClientesRepository()

    def busca_todos_clientes(self):
        clientes = self.repo.busca_todos_clientes()
        return [ClienteResponse(cliente) for cliente in clientes]
