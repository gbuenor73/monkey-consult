from flask import render_template, request, Response
from flask.views import MethodView

from com.monkeyconsulting.adapters.controllers.requests.data_req import DataRequest
from com.monkeyconsulting.adapters.controllers.requests.valor_req import ValorRequest
from com.monkeyconsulting.adapters.controllers.responses.cliente_resp import ClienteResponse
from com.monkeyconsulting.domain.services.clientes_service import ClientesService
from com.monkeyconsulting.domain.services.datas_service import DatasService
from com.monkeyconsulting.domain.services.valor_service import ValorService


class DatasController(MethodView):

    def __init__(self):
        self.repo_cliente = ClientesService()
        self.repo_data = DatasService()
        self.repo_valor = ValorService()

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
            id_valor = formulario.get('id_valor')
            valor_bruto = formulario.get('valor_bruto')
            valor_liquido = formulario.get('valor_liquido')

            dataReq = DataRequest()
            dataReq.id_data = id_data if id_data != '' else None
            dataReq.iniciar_plano_check = iniciar_plano_check == 'on'
            dataReq.mesma_data_check = mesma_data_check == 'on'
            dataReq.data_pagamento = data_pagamento if data_pagamento != '' else None
            dataReq.inicio_plano = inicio_plano if inicio_plano != '' else None

            valorReq = ValorRequest()
            valorReq.id_valor = id_valor if id_valor != '' else None
            valorReq.valor_bruto = valor_bruto if valor_bruto != '' else None
            valorReq.valor_liquido = valor_liquido if valor_liquido != '' else None

            self.repo_data.insere_data(id_cliente, dataReq.to_dto())
            self.repo_valor.insere_data(id_cliente, valorReq.to_dto())

            return Response(f"Sucesso ao atualizar cliente", 200)
        except Exception as e:
            return Response(e.__str__(), 400)
