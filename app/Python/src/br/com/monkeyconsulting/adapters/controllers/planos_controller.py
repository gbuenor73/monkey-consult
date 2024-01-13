from flask import request
from flask.views import MethodView

from src.br.com.monkeyconsulting.adapters.controllers.requests.planos_req import PlanoRequest
from src.br.com.monkeyconsulting.domain.services.planos_service import PlanosService
from src.br.com.monkeyconsulting.domain.utils.utils import list_to_json, format_response


class PlanosController(MethodView):

    def __init__(self):
        self.repo = PlanosService()

    def get(self):
        id = request.args.get('id')
        if id is None:
            planos = self.repo.busca_todos_planos()
            return format_response(list_to_json(planos))
        else:
            dto = self.repo.busca_plano_por_id(id)
            return format_response(dto.to_json())

    def post(self):
        data = request.json
        try:
            dto = PlanoRequest().load(data)
            response = self.repo.insere_plano(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
