from com.monkeyconsulting.domain.services.clientes_service import ClientesService
from com.monkeyconsulting.domain.utils.utils import format_response, list_to_json


class ClientesEntrypoint:

    def __init__(self):
        self.repo = ClientesService()

    def busca_todos_clientes(self):
        clientes_response = self.repo.busca_todos_clientes()
        return format_response(list_to_json(clientes_response))

    def busca_cliente_por_id(self, id):
        cliente_response = self.repo.busca_cliente_por_id(id)
        if cliente_response is None:
            return format_response(list_to_json([]))
        return format_response(cliente_response.to_json())
