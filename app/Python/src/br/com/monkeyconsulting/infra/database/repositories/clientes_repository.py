from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_dto import ClienteDto
from app.Python.src.br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from app.Python.src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel
from br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel


class ClientesRepository:

    def busca_todos_clientes(self):
        with (DBConnectionHandler() as db):
            models = db.session.query(ClienteModel) \
                .join(PlanoModel, PlanoModel.id_plano == ClienteModel.id_dieta) \
                .all()
            return [ClienteDto().to_dto(model) for model in models]

    def busca_cliente_por_id(self, id):
        with DBConnectionHandler() as db:
            model = db.session.query(ClienteModel).filter_by(id_cliente=id).first()
            return ClienteDto().to_dto(model)

    def insere_cliente(self, dto: ClienteDto) -> ClienteDto:
        model = ClienteModel().to_model(dto)
        with (DBConnectionHandler() as db):
            # try:
            db.session.add(model)
            db.session.commit()
            print(model)
            return model
            # except Exception as e:
            #     db.session.rollback()
            #     raise e
        #
        # return ClienteDto().to_dto(model)
