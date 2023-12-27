from app.Python.src.br.com.monkeyconsulting.adapters.controllers.requests.planos_req import PlanoRequest
from app.Python.src.br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from app.Python.src.br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel


class PlanosRepository:
    def busca_todos_planos(self):
        with DBConnectionHandler() as db:
            models = db.session.query(PlanoModel).all()
            return [PlanoRequest().to_request(model) for model in models]

    def busca_plano_por_id(self, id):
        with DBConnectionHandler() as db:
            model = db.session.query(PlanoModel).filter_by(id_plano=id).first()
            return PlanoRequest().to_request(model)

    def insere_plano(self, dto: PlanoRequest) -> PlanoRequest:
        model = PlanoModel().to_model(dto)
        with DBConnectionHandler() as db:
            db.session.add(model)
            db.session.commit()
            return PlanoRequest().to_request(model)
