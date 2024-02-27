from flask import render_template, request, Response
from flask.views import MethodView
from marshmallow.fields import Date

from br.com.monkeyconsulting.adapters.controllers.requests.datas_req import DataRequest
from br.com.monkeyconsulting.adapters.controllers.responses.clientes_resp import ClienteResponse
from br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO
from br.com.monkeyconsulting.domain.services.clientes_service import ClientesService
from src.br.com.monkeyconsulting.domain.services.datas_service import DatasService


class DatasController(MethodView):

    def __init__(self):
        self.repo_data = DatasService()
        self.repo_cliente = ClientesService()

    # def get(self):
    #     id = request.args.get('id')
    #     if id is None:
    #         datas = self.repo.busca_todas_datas()
    #         return format_response(list_to_json(datas))
    #     else:
    #         data = self.repo.busca_data_por_id(id)
    #         if data is not None:
    #             return format_response(data.to_json())
    #         return format_response(list_to_json([]))

    def get(self, id_cliente):
        cliente_dto = self.repo_cliente.busca_cliente_por_id(id_cliente)
        cliente = ClienteResponse().to_resp(cliente_dto)
        cliente.data.transformar_datas()
        return render_template("informa_datas_cliente.html", cliente=cliente.to_json())

    def post(self, id_cliente):
        try:
            formulario = request.form
            data_pagamento = formulario.get('data_pagamento')
            data_inicio_plano_input = formulario.get('data_inicio_plano_input')
            iniciar_plano = formulario.get('iniciar_plano')
            mesma_data = formulario.get('mesma_data')

            if data_pagamento == "":
                raise ValueError("Favor informar a data de pagmento")

            req = DataRequest()
            req.data_pagamento = data_pagamento
            req.inicio_dieta_treino = data_inicio_plano_input

            self.repo_data.insere_data(id_cliente, req.to_dto(), iniciar_plano)
            return Response(f"Sucesso ao atualizar cliente", 200)
        except Exception as e:
            print(e)
            return Response(e.__str__(), 400)

    # def post(self):
    #     data = request.json
    #     try:
    #         dto = DataRequest().load(data)
    #         response = self.repo.insere_data(dto)
    #         return format_response(response.to_json())
    #     except IntegrityError as e:
    #         print(e)
    #         return {'error': 'Cliente não encontrado'}, 400
    #     except Exception as e:
    #         print(e)
    #         return e
