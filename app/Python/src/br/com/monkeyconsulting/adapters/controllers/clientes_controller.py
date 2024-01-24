from flask import request, render_template
from flask.views import MethodView

from br.com.monkeyconsulting.domain.services.dieta_service import DietasTreinosService
from br.com.monkeyconsulting.domain.services.planos_service import PlanosService
from src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_req import ClienteRequest
from src.br.com.monkeyconsulting.domain.services.clientes_service import ClientesService
from src.br.com.monkeyconsulting.domain.utils.utils import format_response, list_to_json


class ClientesController(MethodView):

    def __init__(self):
        self.clientes_service = ClientesService()
        self.planos_service = PlanosService()
        self.dietas_treinos_service = DietasTreinosService()

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

    def get(self, id_cliente=None):
        if id_cliente is None:
            return render_template('form_cliente.html')
        return self.get_editar(id_cliente)

    def delete(self, id_cliente):
        print(f'delete:: {id_cliente}')

    def post(self):
        formulario = request.form

        if 'id_cliente' in formulario:
            print(formulario['id_cliente'])
            return formulario['id_cliente']

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
            response = self.clientes_service.insere_cliente(cliente_request)
            # return format_response(response.to_json())
            return 'Sucesso'
        except Exception as e:
            print(e)
            return e

    def get_editar(self, id_cliente):
        cliente = self.clientes_service.busca_cliente_por_id(id_cliente)
        planos_dto = self.planos_service.busca_todos_planos()
        dietas_treinos_dto = self.dietas_treinos_service.busca_todas_dietas()

        planos = format_response(list_to_json(planos_dto))
        treinos = format_response(list_to_json(dietas_treinos_dto))

        return render_template('editar.html', planos=planos, cliente=cliente, treinos=treinos)
