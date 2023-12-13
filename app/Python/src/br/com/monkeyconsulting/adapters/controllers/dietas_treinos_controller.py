from br.com.monkeyconsulting.adapters.controllers.requests.dietas_treinos_dto import DietaDto
from flask import request
from flask.views import MethodView

from app.Python.src.br.com.monkeyconsulting.infra.database import data_base_repository


class DietasController(MethodView):

    def get(self):
        id = request.args.get('id')
        dto = data_base_repository.busca_dietas_por_id(id)
        return dto.to_json()

    def post(self):
        data = request.json
        try:
            dto = DietaDto().load(data)
            data_base_repository.insere_dieta(dto)

            return dto
        except Exception as e:
            print(e)
            return e
