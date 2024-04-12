from flask import request, render_template, jsonify
from flask.views import MethodView

from com.monkeyconsulting.adapters.controllers.requests.cliente_req import ClienteRequest
from com.monkeyconsulting.adapters.controllers.requests.edit_cliente_req import EditClienteRequest
from com.monkeyconsulting.adapters.controllers.responses.cliente_resp import ClienteResponse
from com.monkeyconsulting.adapters.controllers.responses.dieta_treino_resp import DietaTreinoResponse
from com.monkeyconsulting.adapters.controllers.responses.plano_resp import PlanoResponse
from com.monkeyconsulting.domain.services.clientes_service import ClientesService
from com.monkeyconsulting.domain.services.dieta_service import DietasTreinosService
from com.monkeyconsulting.domain.services.planos_service import PlanosService
from com.monkeyconsulting.domain.utils.utils import format_response, list_to_json


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
            return render_template('insere_cliente.html')
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
                'valor_bruto': formulario['valor_bruto'],
                'valor_liquido': formulario['valor_liquido'],
                'indicador_cliente_ativo': True,
                'id_dieta': 1,
                'id_plano': 1,
            }
        except Exception as e:
            data = request.json

        try:
            req = ClienteRequest().from_json(data)
            self.clientes_service.insere_cliente(req.to_dto())
            # return jsonify(format_response(response.to_json()))
            return "Sucesso", 201
        except Exception as e:
            print(e)
            return e

    def edita_cliente(self, formulario):
        try:
            data = {
                'nome': formulario['nome'],
                'telefone': formulario['telefone'],
                'indicador_cliente_ativo': formulario['indicador_cliente_ativo'],
                'id_cliente': formulario['id_cliente'],
                'id_plano': formulario['id_plano'],
                'id_dieta': formulario['id_dieta'],
            }
        except Exception as e:
            data = request.json

        try:
            req = EditClienteRequest().from_json(data)
            self.clientes_service.edita_cliente(req.to_dto())
            return "Sucesso", 200
        except Exception as e:
            print(e)
            raise e

    def get_editar(self, id_cliente):
        cliente_dto = self.clientes_service.busca_cliente_por_id(id_cliente)
        planos_dto_list = self.planos_service.busca_todos_planos()
        treinos_dto_list = self.dietas_treinos_service.busca_todas_dietas()

        planos_resp_list = [PlanoResponse().dto_to_response(dto) for dto in planos_dto_list]
        treinos_resp_list = [DietaTreinoResponse().dto_to_response(dto) for dto in treinos_dto_list]
        cliente = ClienteResponse().to_resp(cliente_dto)

        planos = format_response(list_to_json(planos_resp_list))
        treinos = format_response(list_to_json(treinos_resp_list))

        return render_template('edita_cliente.html', planos=planos, cliente=cliente, treinos=treinos)
