from app.Python.src.br.com.monkeyconsulting.infra.database import data_base_repository
from br.com.monkeyconsulting.adapters.controllers.requests.cliente_dto import ClienteDto
from br.com.monkeyconsulting.adapters.controllers.requests.datas_dto import DataDto
from flask import request
from flask.views import MethodView


class DatasController(MethodView):

    def get(self):
        id = request.args.get('id')
        dto = data_base_repository.busca_datas_por_id(id)
        return dto.to_json()

    def post(self):
        data = request.json
        try:
            dto = DataDto().load(data)
            data_base_repository.insere_data(dto)
            return dto
        except Exception as e:
            print(e)
            return e
