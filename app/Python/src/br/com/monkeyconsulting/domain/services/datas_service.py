from datetime import timedelta

from br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO
from br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository
from br.com.monkeyconsulting.infra.database.repositories.planos_repository import PlanosRepository
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

    def insere_data(self, id_cliente, data_dto: DataDTO):
        cliente = self.repo_clientes.busca_cliente_por_id(id_cliente)

        if cliente.indicador_cliente_ativo is False:
            raise ValueError("Este cliente não esta ativo.")

        if (data_dto.iniciar_plano_check):
            if (cliente.plano is None or cliente.plano.id_plano == 1):
                raise ValueError("É Necessário selecionar um PLANO primeiro")
            else:
                self.calcular_datas(cliente, data_dto)

        if cliente.data is None or cliente.data.id_data is None:
            data_dto = self.repo_datas.insere_data(data_dto)
            cliente.data = data_dto
            self.repo_clientes.update_cliente(cliente)
        else:
            self.repo_datas.update(data_dto)

    def calcular_datas(self, cliente, data_dto):
        plano = self.repo_planos.busca_plano_por_id(cliente.plano.id_plano)

        if data_dto.iniciar_plano_check and data_dto.mesma_data_check:
            data_dto.inicio_plano = data_dto.data_pagamento

        inicio_plano = data_dto.inicio_plano

        data_dto.vencimento_plano = inicio_plano + timedelta(plano.dias_para_vencimento)
        data_dto.proxima_troca_dieta_treino = inicio_plano + timedelta(plano.dias_para_troca_da_dieta)

        return data_dto
