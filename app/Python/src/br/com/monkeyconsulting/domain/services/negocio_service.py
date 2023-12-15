from br.com.monkeyconsulting.adapters.controllers.responses.response_completo_dto import ResponseCompletoDto
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

    def obtem_todos_dados(self) -> ResponseCompletoDto:
        clientes = self.clientes_repo.busca_todos_clientes()
        datas = self.datas_repo.busca_todas_datas()
        planos = self.planos_repo.busca_todos_planos()
        dietas = self.dietas_repo.busca_todas_dietas()

        list_response = list()

        for cliente in clientes:
            response = ResponseCompletoDto()
            data = [data for data in datas if data.id_cliente == cliente.id_cliente]
            plano = [plano for plano in planos if plano.id_plano == cliente.id_plano]
            dieta = [dieta for dieta in dietas if dieta.id_dieta == cliente.id_dieta]

            response.id_cliente = cliente.id_cliente
            response.nome = cliente.nome
            response.telefone = cliente.telefone
            response.indicador_cliente_ativo = cliente.indicador_cliente_ativo
            response.plano = plano.pop(0).descricao
            response.dieta = dieta.pop(0).descricao
            response.data_pagamento = data[0].data_pagamento
            response.inicio_dieta_treino = data[0].inicio_dieta_treino
            response.ultima_troca_dieta_treino = data[0].ultima_troca_dieta_treino
            response.proxima_troca_dieta_treino = data[0].proxima_troca_dieta_treino
            response.vencimento_plano = data[0].vencimento_plano
            list_response.append(response.to_json())

        return format_response(list_response)

    def post(self):
        return "teste"
