from br.com.monkeyconsulting.adapters.controllers.requests.datas_dto import DataDto
from br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from br.com.monkeyconsulting.infra.database.models.datas_model import DataModel


class DatasRepository:
    def busca_todas_datas(self):
        with DBConnectionHandler() as db:
            models = db.session.query(DataModel).all()
            return [DataDto().to_dto(model) for model in models]

    def busca_datas_por_id(self, id):
        with DBConnectionHandler() as db:
            model = db.session.query(DataModel).filter_by(id_data=id).first()
            return DataDto().to_dto(model)

    def insere_data(self, dto: DataDto) -> DataDto:
        model = DataModel().to_model(dto)
        with DBConnectionHandler() as db:
            models = db.session.add(model).commit()
            return DataDto().to_dto(models)
