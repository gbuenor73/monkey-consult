import http

from br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO
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
            return ClienteResponse().dto_to_resp(cliente_dto)
        return None

    def insere_cliente(self, dto: ClienteDTO):
        self.repo.insere_cliente(dto)

    def edita_cliente(self, dto):
        self.repo.edita_cliente(dto)

    def desativar_cliente(self, id_cliente):
        dto = self.repo.desativar_cliente(id_cliente)
        return http.HTTPStatus.OK
