from flask import request, render_template
from flask.views import MethodView

from src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_req import ClienteRequest
from src.br.com.monkeyconsulting.domain.services.clientes_service import ClientesService
from src.br.com.monkeyconsulting.domain.utils.utils import format_response


class ClientesController(MethodView):

    def __init__(self):
        self.repo = ClientesService()

    # def get(self) -> json:
    #     id = request.args.get('id')
    #     if id is None:
    #         clientes_response = self.repo.busca_todos_clientes()
    #         return format_response(list_to_json(clientes_response))
    #     else:
    #         cliente_response = self.repo.busca_cliente_por_id(id)
    #         if cliente_response is None:
    #             return format_response(list_to_json([]))
    #         return format_response(cliente_response.to_json())

    def get(self):
        return render_template('form_cliente.html')

    def post(self):
        formulario = request.form

        try:
            data = {
                'nome': formulario['nome'],
                'telefone': formulario['telefone'],
                'id_plano': 4,  # alterar para nao obrigatorio
                'id_dieta': 2,  # alterar para nao obrigatorio
                'indicador_cliente_ativo': 1  # manter

            }
        except Exception as e:
            data = request.json

        try:
            cliente_request = ClienteRequest().load(data)
            response = self.repo.insere_cliente(cliente_request)
            # return format_response(response.to_json())
            return 'Sucesso'
        except Exception as e:
            print(e)
            return e
