from flask import Flask
from src.br.com.monkeyconsulting.infra.database.operations import fetch_data

app = Flask(__name__)


@app.route('/')
def get():

    query='SELECT * FROM CLIENTES'
    data = fetch_data(query)
    return data
    # if data:
    #     for row in data:
    #         print(row)
    #
    # return 'GET!'


@app.route('/', methods=['POST'])
def post():
    return 'POST'


if __name__ == '__main__':
    app.run(debug=True)
