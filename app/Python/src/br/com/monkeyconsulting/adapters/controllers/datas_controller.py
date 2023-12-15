from flask import request
from flask.views import MethodView

from br.com.monkeyconsulting.adapters.controllers.requests.datas_dto import DataDto
from br.com.monkeyconsulting.domain.utils.utils import list_to_json, format_response
from br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository
from br.com.monkeyconsulting.infra.database.repositories.datas_repository import DatasRepository


class DatasController(MethodView):

    def __init__(self):
        self.repo = DatasRepository()

    def get(self):
        id = request.args.get('id')
        if id is None:
            datas = self.repo.busca_todas_datas()
            return format_response(list_to_json(datas))
        else:
            data = self.repo.busca_datas_por_id(id)
            return format_response(data.to_json())

    def post(self):
        data = request.json
        try:
            dto = DataDto().load(data)
            response = self.repo.insere_data(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
