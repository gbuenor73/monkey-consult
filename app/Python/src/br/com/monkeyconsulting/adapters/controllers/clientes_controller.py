import json

from flask import request
from flask.views import MethodView

from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_req import ClienteRequest
from br.com.monkeyconsulting.domain.services.clientes_service import ClientesService
from br.com.monkeyconsulting.domain.utils.utils import list_to_json, format_response
from br.com.monkeyconsulting.infra.database.repositories.clientes_repository import ClientesRepository


class ClientesController(MethodView):

    def __init__(self):
        self.repo = ClientesService()

    def get(self) -> json:
        id = request.args.get('id')
        if id is None:
            clientes = self.repo.busca_todos_clientes()
            return format_response(list_to_json(clientes))
        else:
            dto = self.repo.busca_cliente_por_id(id)
            return format_response(dto.to_json())

    def post(self):
        data = request.json
        try:
            dto = ClienteRequest().load(data)
            response = self.repo.insere_cliente(dto)
            return format_response(response.to_json())
        except Exception as e:
            print(e)
            return e
