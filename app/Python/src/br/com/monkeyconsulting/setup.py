from flask import Flask
from flask_cors import CORS

from br.com.monkeyconsulting.adapters.controllers.default_controller import Defaultcontroller
from src.br.com.monkeyconsulting.adapters.controllers.clientes_controller import ClientesController
from src.br.com.monkeyconsulting.adapters.controllers.datas_controller import DatasController
from src.br.com.monkeyconsulting.adapters.controllers.dietas_treinos_controller import DietasController
from src.br.com.monkeyconsulting.adapters.controllers.negocios_controller import NegocioController
from src.br.com.monkeyconsulting.adapters.controllers.planos_controller import PlanosController

app = Flask(__name__, static_folder='front/static', template_folder='front/templates')
CORS(app)

app.add_url_rule('/', view_func=NegocioController.as_view('negocio'))
app.add_url_rule('/planos', view_func=PlanosController.as_view('planos'))
app.add_url_rule('/dietas', view_func=DietasController.as_view('dietas'))
app.add_url_rule('/datas', view_func=DatasController.as_view('datas'))
app.add_url_rule('/default/<string:pagina>', view_func=Defaultcontroller.as_view('header_footer'))
app.add_url_rule('/clientes', view_func=ClientesController.as_view('listar_clientes'))
app.add_url_rule('/clientes/<int:id_cliente>', view_func=ClientesController.as_view('deletar_clientes'))
app.add_url_rule('/clientes/editar', view_func=ClientesController.as_view('editar_cliente'))
app.add_url_rule('/clientes/editar/<int:id_cliente>', view_func=ClientesController.as_view('detalhar_cliente'))

if __name__ == '__main__':
    app.run(debug=True)
