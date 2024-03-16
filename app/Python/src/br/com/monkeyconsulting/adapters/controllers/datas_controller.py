from flask import render_template, request, Response
from flask.views import MethodView

from br.com.monkeyconsulting.adapters.controllers.requests.data_req import DataRequest
from br.com.monkeyconsulting.adapters.controllers.responses.cliente_resp import ClienteResponse
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
            id_data = formulario.get('id_data')
            data_pagamento = formulario.get('data_pagamento')
            iniciar_plano_check = formulario.get('iniciar_plano_check')
            mesma_data_check = formulario.get('mesma_data_check')
            inicio_plano = formulario.get('inicio_plano')

            req = DataRequest()
            req.id_data = id_data if id_data != '' else None
            req.iniciar_plano_check = iniciar_plano_check == 'on'
            req.mesma_data_check = mesma_data_check == 'on'
            req.data_pagamento = data_pagamento if data_pagamento != '' else None
            req.inicio_plano = inicio_plano if inicio_plano != '' else None

            self.repo_data.insere_data(id_cliente, req.to_dto())

            return Response(f"Sucesso ao atualizar cliente", 200)
        except Exception as e:
            return Response(e.__str__(), 400)
