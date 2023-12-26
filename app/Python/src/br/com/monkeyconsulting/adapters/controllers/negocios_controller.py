from flask.views import MethodView

from br.com.monkeyconsulting.domain.services.negocio_service import NegocioService


class NegocioController(MethodView):

    def __init__(self):
        self.service = NegocioService()

    def get(self):
        return self.service.obtem_todos_dados()

    # def post(self):
    #     return self.service.post()
