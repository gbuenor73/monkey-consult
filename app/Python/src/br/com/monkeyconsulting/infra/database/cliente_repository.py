from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_dto import ClienteDto
from app.Python.src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel

db_config = {
    'host': "localhost",
    'user': "monkey",
    'password': "monkey",
    'database': "monkey_consulting"
}

engine = create_engine(
    f"mysql+mysqlconnector://{db_config.get('user')}:{db_config.get('password')}@localhost/{db_config.get('database')}")

Session = sessionmaker(bind=engine)
session = Session()


def busca_cliente_por_id(id):
    model = session.query(ClienteModel).filter_by(id_cliente=id).first()
    return ClienteDto().to_dto(model)


def insere_cliente(dto: ClienteDto) -> None:
    model = ClienteModel().to_model(dto)
    print(model)
    session.add(model)
    session.commit()
