from br.com.monkeyconsulting.adapters.controllers.requests.dietas_treinos_dto import DietaDto
from br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from br.com.monkeyconsulting.infra.database.models.dietas_treinos_model import DietaTreinoModel


class DietasRepository:
    def busca_todas_dietas(self):
        with DBConnectionHandler() as db:
            models = db.session.query(DietaTreinoModel).all()
            return [DietaDto().to_dto(model) for model in models]

    def busca_dietas_por_id(self, id):
        with DBConnectionHandler() as db:
            model = db.session.query(DietaTreinoModel).filter_by(id_dieta=id).first()
            return DietaDto().to_dto(model)

    def insere_dieta(self, dto: DietaDto) -> DietaDto:
        model = DietaTreinoModel().to_model(dto)
        with DBConnectionHandler() as db:
            models = db.session.add(model).commit()
            return DietaDto().to_dto(models)
