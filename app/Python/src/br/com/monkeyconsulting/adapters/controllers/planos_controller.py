from flask import request
from flask.views import MethodView

from app.Python.src.br.com.monkeyconsulting.infra.database import data_base_repository
from br.com.monkeyconsulting.adapters.controllers.requests.planos_dto import PlanoDto
from br.com.monkeyconsulting.domain.utils.utils import list_to_json, format_response


class PlanosController(MethodView):

    def get(self):
        id = request.args.get('id')
        if id is None:
            planos = data_base_repository.busca_todos_planos()
            return format_response(list_to_json(planos))
        else:
            dto = data_base_repository.busca_planos_por_id(id)
            return format_response(dto.to_json())

    def post(self):
        data = request.json
        try:
            dto = PlanoDto().load(data)
            response = data_base_repository.insere_plano(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
