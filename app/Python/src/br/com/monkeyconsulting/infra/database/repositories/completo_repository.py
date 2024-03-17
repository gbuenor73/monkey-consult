from src.br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel


class CompletoRepository:

    def busca_completa(self):
        with DBConnectionHandler() as db:
            models = db.session.query(ClienteModel).filter_by(indicador_cliente_ativo=True).all()
            if models is not None:
                return [model.to_dto() for model in models]
            return []
