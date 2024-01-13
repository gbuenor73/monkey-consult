from src.br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO
from src.br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel


class ClientesRepository:

    def busca_todos_clientes(self):
        with (DBConnectionHandler() as db):
            models = db.session.query(ClienteModel).all()
            if models is not None:
                return [ClienteDTO().to_dto(model) for model in models]
            return []

    def busca_cliente_por_id(self, id):
        with DBConnectionHandler() as db:
            model = db.session.query(ClienteModel).filter_by(id_cliente=id).first()
            if model is not None:
                return ClienteDTO().to_dto(model)
            return None

    def insere_cliente(self, dto: ClienteDTO) -> ClienteDTO:
        model = ClienteModel().to_model(dto)
        with (DBConnectionHandler() as db):
            try:
                db.session.add(model)
                db.session.commit()
                return ClienteDTO().to_dto(model)
            except Exception as e:
                db.session.rollback()
                raise e
