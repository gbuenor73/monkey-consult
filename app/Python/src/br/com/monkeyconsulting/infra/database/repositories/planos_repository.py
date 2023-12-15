from br.com.monkeyconsulting.adapters.controllers.requests.planos_dto import PlanoDto
from br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel


class PlanosRepository:
    def busca_todos_planos(self):
        with DBConnectionHandler() as db:
            models = db.session.query(PlanoModel).all()
            return [PlanoDto().to_dto(model) for model in models]

    def busca_planos_por_id(self, id):
        with DBConnectionHandler() as db:
            model = db.session.query(PlanoModel).filter_by(id_plano=id).first()
            return PlanoDto().to_dto(model)

    def insere_plano(self, dto: PlanoDto) -> PlanoDto:
        model = PlanoModel().to_model(dto)
        with DBConnectionHandler() as db:
            models = db.session.add(model).commit()
            return PlanoDto().to_dto(models)
