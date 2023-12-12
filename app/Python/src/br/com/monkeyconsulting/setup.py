from flask import Flask

from app.Python.src.br.com.monkeyconsulting.adapters.controllers.clientes_controller import ClientesController
from br.com.monkeyconsulting.adapters.controllers.datas_controller import DatasController
from br.com.monkeyconsulting.adapters.controllers.dietas_treinos_controller import DietasController
from br.com.monkeyconsulting.adapters.controllers.planos_controller import PlanosController

app = Flask(__name__)

app.add_url_rule('/clientes', view_func=ClientesController.as_view('clientes'))
app.add_url_rule('/planos', view_func=PlanosController.as_view('planos'))
app.add_url_rule('/dietas', view_func=DietasController.as_view('dietas'))
app.add_url_rule('/datas', view_func=DatasController.as_view('datas'))

if __name__ == '__main__':
    app.run('/monkey', 8081, True)
