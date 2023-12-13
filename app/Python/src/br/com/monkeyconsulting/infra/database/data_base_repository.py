from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_dto import ClienteDto
from app.Python.src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel
from br.com.monkeyconsulting.adapters.controllers.requests.datas_dto import DataDto
from br.com.monkeyconsulting.adapters.controllers.requests.dietas_treinos_dto import DietaDto
from br.com.monkeyconsulting.adapters.controllers.requests.planos_dto import PlanoDto
from br.com.monkeyconsulting.infra.database.models.datas_model import DataModel
from br.com.monkeyconsulting.infra.database.models.dietas_treinos_model import DietaTreinoModel
from br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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


def busca_todos_clientes():
    models = session.query(ClienteModel).all()
    return [ClienteDto().to_dto(model) for model in models]


def busca_cliente_por_id(id):
    model = session.query(ClienteModel).filter_by(id_cliente=id).first()
    return ClienteDto().to_dto(model)


def busca_planos_por_id(id):
    model = session.query(PlanoModel).filter_by(id_plano=id).first()
    return PlanoDto().to_dto(model)


def busca_datas_por_id(id):
    model = session.query(DataModel).filter_by(id_datas=id).first()
    return DataDto().to_dto(model)


def busca_dietas_por_id(id):
    model = session.query(DietaTreinoModel).filter_by(id_dieta=id).first()
    return DietaDto().to_dto(model)


def insere_cliente(dto: ClienteDto) -> None:
    model = ClienteModel().to_model(dto)
    session.add(model)
    session.commit()


def insere_data(dto: DataDto) -> None:
    model = DataModel().to_model(dto)
    session.add(model)
    session.commit()


def insere_dieta(dto: DietaDto) -> None:
    model = DietaTreinoModel().to_model(dto)
    session.add(model)
    session.commit()


def insere_plano(dto: PlanoDto) -> None:
    model = PlanoModel().to_model(dto)
    session.add(model)
    session.commit()
