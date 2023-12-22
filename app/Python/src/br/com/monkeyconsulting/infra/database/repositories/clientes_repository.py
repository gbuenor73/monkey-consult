from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.cliente_req import ClienteRequest
from app.Python.src.br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from app.Python.src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel
from br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO


class ClientesRepository:

    def busca_todos_clientes(self):
        with (DBConnectionHandler() as db):
            models = db.session.query(ClienteModel).all()
            return [ClienteDTO.to_dto(model) for model in models]

    def busca_cliente_por_id(self, models=id):
        with DBConnectionHandler() as db:
            model = db.session.query(ClienteModel).filter_by(id_cliente=id).first()
            return ClienteRequest().to_req(model)

    def insere_cliente(self, dto: ClienteRequest) -> ClienteRequest:
        model = ClienteModel().to_model(dto)
        with (DBConnectionHandler() as db):
            try:
                db.session.add(model)
                db.session.commit()
                print(model)
                return ClienteRequest().to_req(model)
            except Exception as e:
                db.session.rollback()
                raise e
