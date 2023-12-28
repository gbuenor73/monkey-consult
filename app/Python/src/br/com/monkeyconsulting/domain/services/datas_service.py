from src.br.com.monkeyconsulting.adapters.controllers.responses.data_resp import DataResponse
from src.br.com.monkeyconsulting.infra.database.repositories.datas_repository import DatasRepository


class DatasService:

    def __init__(self):
        self.repo = DatasRepository()

    def busca_todas_datas(self):
        datas = self.repo.busca_todas_datas()
        return [DataResponse(data) for data in datas]

    def busca_data_por_id(self, id):
        data = self.repo.busca_datas_por_id(id)
        if data is not None:
            return DataResponse(data)
        return None

    def insere_data(self, dto):
        dto_response = self.repo.insere_data(dto)
        return DataResponse(dto_response)
