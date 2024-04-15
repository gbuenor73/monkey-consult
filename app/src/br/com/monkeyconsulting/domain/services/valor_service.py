from com.monkeyconsulting.domain.dtos.valor_dto import ValorDTO
from com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository
from com.monkeyconsulting.infra.database.repositories.valor_repository import ValorRepository


class ValorService:

    def __init__(self):
        self.repo_valor = ValorRepository()
        self.repo_cliente = ClientesRepository()

    def insere_data(self, valor_dto: ValorDTO):
        cliente_dto = self.repo_cliente.busca_cliente_por_id(valor_dto.cliente.id)

        if cliente_dto is not None and cliente_dto.id is not None:
            self.repo_valor.insere_valor(valor_dto)
        else:
            raise Exception("Não foi encontrado o cliente informado", valor_dto.cliente.id)

