from br.com.monkeyconsulting.domain.dtos.plano_dto import PlanoDTO
from src.br.com.monkeyconsulting.adapters.controllers.requests.planos_req import PlanoRequest
from src.br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from src.br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel


class PlanosRepository:
    def busca_todos_planos(self):
        with DBConnectionHandler() as db:
            models = db.session.query(PlanoModel).all()
            return [model.to_dto() for model in models]

    def busca_plano_por_id(self, id) -> PlanoDTO:
        with DBConnectionHandler() as db:
            model = db.session.query(PlanoModel).filter_by(id_plano=id).first()
            return model.to_dto()

    def insere_plano(self, dto: PlanoDTO) -> PlanoDTO:
        model = PlanoModel().to_model(dto)
        with DBConnectionHandler() as db:
            db.session.add(model)
            db.session.commit()
            return model.to_dto()
