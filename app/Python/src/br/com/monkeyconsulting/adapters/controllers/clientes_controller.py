import json

from flask import request
from flask.views import MethodView

from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_dto import ClienteDto
from app.Python.src.br.com.monkeyconsulting.infra.database import data_base_repository
from br.com.monkeyconsulting.domain.utils.utils import list_to_json, format_response


class ClientesController(MethodView):

    def get(self) -> json:
        id = request.args.get('id')
        if id is None:
            clientes = data_base_repository.busca_todos_clientes()
            return format_response(list_to_json(clientes))
        else:
            dto = data_base_repository.busca_cliente_por_id(id)
            return format_response(dto.to_json())

    def post(self):
        data = request.json
        try:
            dto = ClienteDto().load(data)
            response = data_base_repository.insere_cliente(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
