from flask import render_template, request
from flask.views import MethodView

from br.com.monkeyconsulting.domain.services.clientes_service import ClientesService
from src.br.com.monkeyconsulting.domain.services.datas_service import DatasService


class DatasController(MethodView):

    def __init__(self):
        self.repo = DatasService()
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
        return render_template("informa_datas_cliente.html", cliente=cliente_dto.to_json())

    def post(self, id_cliente):
        ass = request.form

        return f"{id_cliente}"

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
