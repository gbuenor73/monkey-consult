from br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO
from br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository
from br.com.monkeyconsulting.infra.database.repositories.planos_repository import PlanosRepository
from src.br.com.monkeyconsulting.adapters.controllers.responses.data_resp import DataResponse
from src.br.com.monkeyconsulting.infra.database.repositories.datas_repository import DatasRepository


class DatasService:

    def __init__(self):
        self.repo_datas = DatasRepository()
        self.repo_clientes = ClientesRepository()
        self.repo_planos = PlanosRepository()

    def busca_todas_datas(self):
        return self.repo_datas.busca_todas_datas()

    def busca_data_por_id(self, id):
        return self.repo_datas.busca_datas_por_id(id)

    def insere_data(self, id_cliente, dto: DataDTO, iniciar_plano):
        cliente = self.repo_clientes.busca_cliente_por_id(id_cliente)

        # if cliente.data is not None:
        #     raise ValueError("A data de pagamento ja foi informada")

        if cliente.indicador_cliente_ativo is False:
            raise ValueError("Este cliente não esta ativo.")

        if cliente.plano is None or cliente.plano.id_plano == 1:
            raise ValueError("É Necessário selecionar um PLANO primeiro")

        if cliente.data is None or cliente.data.id_data:
            dto.id_data = cliente.data.id_data
            data_dto = self.repo_datas.update(dto)
        else:
            data_dto = self.repo_datas.insere_data(dto)

        if iniciar_plano == 'on':
            data_dto.inicio_dieta_treino = dto.data_pagamento
            self.calcular_datas(cliente, data_dto)

        cliente.data = data_dto
        self.repo_clientes.update_cliente(cliente)

    def calcular_datas(self, cliente, data_dto):
        plano = self.repo_planos.busca_plano_por_id(cliente.plano.id_plano)
        dias_para_vencimento = plano.dias_para_vencimento
        dias_para_troca = plano.dias_para_troca_da_dieta

        # data_dto.

        vencimento_plano = plano.inicio_dieta_trerin

        return data_dto
