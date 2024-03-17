from src.br.com.monkeyconsulting.adapters.controllers.requests.dieta_treinos_req import DietaRequest
from src.br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from src.br.com.monkeyconsulting.infra.database.models.dietas_treinos_model import DietaTreinoModel


class DietasRepository:
    def busca_todas_dietas(self):
        with DBConnectionHandler() as db:
            models = db.session.query(DietaTreinoModel).all()
            return [DietaRequest().to_request(model) for model in models]

    def busca_dietas_por_id(self, id):
        with DBConnectionHandler() as db:
            model = db.session.query(DietaTreinoModel).filter_by(id_dieta=id).first()
            return DietaRequest().to_request(model)

    def insere_dieta(self, dto: DietaRequest) -> DietaRequest:
        model = DietaTreinoModel().to_model(dto)
        with DBConnectionHandler() as db:
            db.session.add(model)
            db.session.commit()
            return DietaRequest().to_request(model)
