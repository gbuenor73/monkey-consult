from flask import request
from flask.views import MethodView

from br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository
from br.com.monkeyconsulting.adapters.controllers.requests.planos_dto import PlanoDto
from br.com.monkeyconsulting.domain.utils.utils import list_to_json, format_response
from br.com.monkeyconsulting.infra.database.repositories.planos_repository import PlanosRepository


class PlanosController(MethodView):

    def __init__(self):
        self.repo = PlanosRepository()

    def get(self):
        id = request.args.get('id')
        if id is None:
            planos = self.repo.busca_todos_planos()
            return format_response(list_to_json(planos))
        else:
            dto = self.repo.busca_planos_por_id(id)
            return format_response(dto.to_json())

    def post(self):
        data = request.json
        try:
            dto = PlanoDto().load(data)
            response = self.repo.insere_plano(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
