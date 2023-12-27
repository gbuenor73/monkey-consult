import json

from flask import request
from flask.views import MethodView

from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.dietas_treinos_req import DietaRequest
from app.Python.src.br.com.monkeyconsulting.domain.services.dieta_service import DietaTreinoService
from app.Python.src.br.com.monkeyconsulting.domain.utils.utils import format_response, list_to_json


class DietasController(MethodView):

    def __init__(self):
        self.repo = DietaTreinoService()

    def get(self) -> json:
        id = request.args.get('id')
        if id is None:
            dietas = self.repo.busca_todas_dietas()
            return format_response(list_to_json(dietas))
        else:
            dto = self.repo.busca_dieta_por_id(id)
            return format_response(dto.to_json())

    def post(self):
        data = request.json
        try:
            dto = DietaRequest().load(data)
            response = self.repo.insere_dieta(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
