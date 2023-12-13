from br.com.monkeyconsulting.adapters.controllers.requests.planos_dto import PlanoDto
from br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel
from flask import request
from flask.views import MethodView

from app.Python.src.br.com.monkeyconsulting.infra.database import data_base_repository


class PlanosController(MethodView):

    def get(self):
        id = request.args.get('id')
        dto = data_base_repository.busca_planos_por_id(id)
        return dto.to_json()

    def post(self):
        data = request.json
        try:
            dto = PlanoDto().load(data)
            data_base_repository.insere_plano(dto)

            return dto
        except Exception as e:
            print(e)
            return e
