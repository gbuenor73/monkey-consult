from flask import render_template
from flask.views import MethodView

from src.br.com.monkeyconsulting.domain.services.negocio_service import NegocioService
from src.br.com.monkeyconsulting.domain.utils.utils import format_response, list_to_json


class NegocioController(MethodView):

    def __init__(self):
        self.service = NegocioService()

    def get(self):
        # response = self.service.obtem_todos_dados()
        # return format_response(list_to_json(response))
        return render_template("index.html")
