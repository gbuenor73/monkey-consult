import http

from com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO
from com.monkeyconsulting.adapters.controllers.responses.cliente_resp import ClienteResponse
from com.monkeyconsulting.domain.dtos.valor_dto import ValorDTO
from com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository
from com.monkeyconsulting.infra.database.repositories.valor_repository import ValorRepository


class ClientesService:

    def __init__(self):
        self.client_repo = ClientesRepository()
        self.valor_repo = ValorRepository()

    def busca_todos_clientes(self):
        clientes = self.client_repo.busca_todos_clientes()

        if clientes is not None:
            return [ClienteResponse(cliente) for cliente in clientes]
        return []

    def busca_cliente_por_id(self, id_cliente):
        return self.client_repo.busca_cliente_por_id(id_cliente)

    def insere_cliente(self, cliente_dto: ClienteDTO, valor_dto: ValorDTO):
        cliente_dto = self.client_repo.insere_cliente(cliente_dto)

        valor_dto.id_valor = cliente_dto.id
        self.valor_repo.insere_valor(valor_dto)

    def edita_cliente(self, dto: ClienteDTO):
        self.client_repo.edita_cliente(dto)

    def desativar_cliente(self, id_cliente):
        dto = self.client_repo.desativar_cliente(id_cliente)
        return http.HTTPStatus.OK
