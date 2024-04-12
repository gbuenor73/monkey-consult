from flask import Flask
from flask_cors import CORS

from com.monkeyconsulting.adapters.controllers.clientes_controller import ClientesController
from com.monkeyconsulting.adapters.controllers.datas_controller import DatasController

from com.monkeyconsulting.adapters.controllers.dietas_treinos_controller import DietasController
from com.monkeyconsulting.adapters.controllers.negocios_controller import NegocioController
from com.monkeyconsulting.adapters.controllers.planos_controller import PlanosController

app = Flask(__name__, static_folder='front/static', template_folder='front/templates')
CORS(app)

app.add_url_rule('/', view_func=NegocioController.as_view('negocio'))
app.add_url_rule('/planos', view_func=PlanosController.as_view('planos'))
app.add_url_rule('/dietas', view_func=DietasController.as_view('dietas'))
app.add_url_rule('/datas', view_func=DatasController.as_view('datas'))

app.add_url_rule('/clientes', view_func=ClientesController.as_view('listar_clientes'))
app.add_url_rule('/cliente', view_func=ClientesController.as_view('cria_cliente'))
app.add_url_rule('/cliente', view_func=ClientesController.as_view('edita_cliente'))
app.add_url_rule('/cliente/<int:id_cliente>', view_func=ClientesController.as_view('deletar_clientes'))
app.add_url_rule('/cliente/detalhar/<int:id_cliente>', view_func=ClientesController.as_view('detalhar_cliente'))
app.add_url_rule('/cliente/pagamento/<int:id_cliente>', view_func=DatasController.as_view('pagamento_cliente'))


@app.route('/favicon.ico')
def favico():
    return app.send_static_file('empty.ico')


if __name__ == '__main__':
    app.run(debug=True)
