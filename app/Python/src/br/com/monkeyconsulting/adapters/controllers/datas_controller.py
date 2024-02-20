from flask import render_template, request, Response
from flask.views import MethodView

from br.com.monkeyconsulting.adapters.controllers.responses.clientes_resp import ClienteResponse
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
        cliente = ClienteResponse().dto_to_resp(cliente_dto)
        return render_template("informa_datas_cliente.html", cliente=cliente.to_json())

    def post(self, id_cliente):
        try:
            formulario = request.form
            data_pagamento = formulario.get('data_pagamento')
            iniciar_plano = formulario.get('iniciar_plano')

            if data_pagamento == "":
                raise ValueError("Favor informar a data de pagmento")

            self.repo_data.insere_data(id_cliente, data_pagamento, iniciar_plano)
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
