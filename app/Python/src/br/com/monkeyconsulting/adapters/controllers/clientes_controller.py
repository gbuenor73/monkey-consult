import json

from flask import request, render_template, jsonify
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
        try:
            self.clientes_service.desativar_cliente(id_cliente)
            return jsonify(), 200
        except Exception as e:
            return jsonify(f'Erro interno: {e} '), 500

    def post(self):
        if request.form.get('_method') == 'PATCH':
            return self.edita_cliente(request.form)
        return self.cria_cliente(request.form)

    def cria_cliente(self, formulario):

        try:
            data = {
                'nome': formulario['nome'],
                'telefone': formulario['telefone'],
                'indicador_cliente_ativo': True
            }
        except Exception as e:
            data = request.json

        try:
            cliente_request = ClienteRequest().load(data)
            response = self.clientes_service.insere_cliente(cliente_request)
            # return jsonify(format_response(response.to_json()))
            return "Sucesso", 201
        except Exception as e:
            print(e)
            return e

    def edita_cliente(self, formulario):
        try:

            plano = json.load(formulario['plano'])

            data = {
                'id_cliente': formulario['id_cliente'],
                'data': formulario['nome'],
                'telefone': formulario['telefone'],
                'plano': formulario['plano'],
                'treino': formulario['treino'],
                'id_plano': formulario['plano'],
                'id_dieta': formulario['treino']
            }
        except Exception as e:
            data = request.json

        try:
            cliente_request = ClienteRequest.load(data)
            print(cliente_request)
        except Exception as e:
            print(e)
            raise e

        return 'teste', 200

    def get_editar(self, id_cliente):
        cliente = self.clientes_service.busca_cliente_por_id(id_cliente)
        planos_dto = self.planos_service.busca_todos_planos()
        dietas_treinos_dto = self.dietas_treinos_service.busca_todas_dietas()

        planos = format_response(list_to_json(planos_dto))
        treinos = format_response(list_to_json(dietas_treinos_dto))

        return render_template('editar.html', planos=planos, cliente=cliente, treinos=treinos)
