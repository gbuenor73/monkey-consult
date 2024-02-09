from br.com.monkeyconsulting.domain.dtos.cliente_dto import ClienteDTO
from src.br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel


class CompletoRepository:

    def busca_completa(self):
        with DBConnectionHandler() as db:
            models = db.session.query(ClienteModel).filter_by(indicador_cliente_ativo=True).all()
            if models is not None:
                return [ClienteDTO().from_model_to_dto(model) for model in models]
            return []
