from flask import Flask

from app.Python.src.br.com.monkeyconsulting.adapters.controllers.controller import ClientesController

app = Flask(__name__)

app.add_url_rule('/clientes', view_func=ClientesController.as_view('clientes'))

if __name__ == '__main__':
    app.run(debug=True)
