from flask import request
from flask.views import MethodView

from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.datas_req import DataRequest
from app.Python.src.br.com.monkeyconsulting.domain.services.datas_service import DatasService
from app.Python.src.br.com.monkeyconsulting.domain.utils.utils import list_to_json, format_response


class DatasController(MethodView):

    def __init__(self):
        self.repo = DatasService()

    def get(self):
        id = request.args.get('id')
        if id is None:
            datas = self.repo.busca_todas_datas()
            return format_response(list_to_json(datas))
        else:
            data = self.repo.busca_data_por_id(id)
            return format_response(data.to_json())

    def post(self):
        data = request.json
        try:
            dto = DataRequest().load(data)
            response = self.repo.insere_data(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
