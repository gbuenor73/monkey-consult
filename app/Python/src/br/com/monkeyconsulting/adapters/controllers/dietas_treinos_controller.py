from flask import request
from flask.views import MethodView

from br.com.monkeyconsulting.adapters.controllers.requests.dietas_treinos_dto import DietaDto
from br.com.monkeyconsulting.domain.utils.utils import format_response, list_to_json
from br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository
from br.com.monkeyconsulting.infra.database.repositories.dieta_repository import DietasRepository


class DietasController(MethodView):

    def __init__(self):
        self.repo = DietasRepository()

    def get(self):
        id = request.args.get('id')
        if id is None:
            dietas = self.repo.busca_todas_dietas()
            return format_response(list_to_json(dietas))
        else:
            dto = self.repo.busca_dietas_por_id(id)
            return format_response(dto.to_json())

    def post(self):
        data = request.json
        try:
            dto = DietaDto().load(data)
            response = self.repo.insere_dieta(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
