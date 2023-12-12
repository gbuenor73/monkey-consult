from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_dto import ClienteDto
from app.Python.src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel
from br.com.monkeyconsulting.adapters.controllers.requests.datas_dto import DatasDto
from br.com.monkeyconsulting.adapters.controllers.requests.dietas_treinos_dto import DietasDto
from br.com.monkeyconsulting.adapters.controllers.requests.planos_dto import PlanosDto
from br.com.monkeyconsulting.infra.database.models.datas_model import DataModel
from br.com.monkeyconsulting.infra.database.models.dietas_treinos_model import DietaTreinoModel
from br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel

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


def busca_planos_por_id(id):
    model = session.query(PlanoModel).filter_by(id_plano=id).first()
    return PlanosDto().to_dto(model)


def busca_datas_por_id(id):
    model = session.query(DataModel).filter_by(id_datas=id).first()
    return DatasDto().to_dto(model)


def busca_dietas_por_id(id):
    model = session.query(DietaTreinoModel).filter_by(id_dieta=id).first()
    return DietasDto().to_dto(model)


def insere_cliente(dto: ClienteDto) -> None:
    model = ClienteModel().to_model(dto)
    session.add(model)
    session.commit()
