from src.br.com.monkeyconsulting.adapters.controllers.responses.clientes_resp import ClienteResponse
from src.br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository


class ClientesService:

    def __init__(self):
        self.repo = ClientesRepository()

    def busca_todos_clientes(self):
        clientes = self.repo.busca_todos_clientes()

        if clientes is not None:
            return [ClienteResponse(cliente) for cliente in clientes]
        return []

    def busca_cliente_por_id(self, id_cliente):
        cliente_dto = self.repo.busca_cliente_por_id(id_cliente)
        if cliente_dto is not None:
            return ClienteResponse(cliente_dto)
        return None

    def insere_cliente(self, dto):
        dto_response = self.repo.insere_cliente(dto)
        return ClienteResponse(dto_response)
