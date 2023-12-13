from flask import request
from flask.views import MethodView

from app.Python.src.br.com.monkeyconsulting.infra.database import data_base_repository
from br.com.monkeyconsulting.adapters.controllers.requests.dietas_treinos_dto import DietaDto
from br.com.monkeyconsulting.domain.utils.utils import format_response, list_to_json


class DietasController(MethodView):

    def get(self):
        id = request.args.get('id')
        if id is None:
            dietas = data_base_repository.busca_todas_dietas()
            return format_response(list_to_json(dietas))
        else:
            dto = data_base_repository.busca_dietas_por_id(id)
            return format_response(dto.to_json())

    def post(self):
        data = request.json
        try:
            dto = DietaDto().load(data)
            response = data_base_repository.insere_dieta(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
