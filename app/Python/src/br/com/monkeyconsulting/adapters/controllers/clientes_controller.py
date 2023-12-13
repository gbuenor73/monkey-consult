from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_dto import ClienteDto
from app.Python.src.br.com.monkeyconsulting.infra.database import data_base_repository
from flask import request
from flask.views import MethodView


class ClientesController(MethodView):

    def get(self):
        id = request.args.get('id')
        dto = data_base_repository.busca_cliente_por_id(id)
        return dto.to_json()

    def post(self):
        data = request.json
        try:
            dto = ClienteDto().load(data)
            data_base_repository.insere_cliente(dto)

            return dto
        except Exception as e:
            print(e)
            return e
