import json

from flask import request
from flask.views import MethodView

from app.Python.src.br.com.monkeyconsulting.infra.database import data_base_repository
from br.com.monkeyconsulting.adapters.controllers.requests.datas_dto import DataDto
from br.com.monkeyconsulting.domain.utils.utils import list_to_json, date_handler, format_response


class DatasController(MethodView):

    def get(self):
        id = request.args.get('id')
        if id is None:
            datas = data_base_repository.busca_todas_datas()
            return format_response(list_to_json(datas))
        else:
            data = data_base_repository.busca_datas_por_id(id)
            return format_response(data.to_json())

    def post(self):
        data = request.json
        try:
            dto = DataDto().load(data)
            response = data_base_repository.insere_data(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
