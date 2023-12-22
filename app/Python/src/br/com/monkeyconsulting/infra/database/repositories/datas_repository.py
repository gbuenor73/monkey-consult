from br.com.monkeyconsulting.adapters.controllers.requests.datas_req import DataRequest
from br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from br.com.monkeyconsulting.infra.database.models.datas_model import DataModel


class DatasRepository:
    def busca_todas_datas(self):
        with DBConnectionHandler() as db:
            models = db.session.query(DataModel).all()
            return [DataRequest().to_request(model) for model in models]

    def busca_datas_por_id(self, id):
        with DBConnectionHandler() as db:
            model = db.session.query(DataModel).filter_by(id_data=id).first()
            return DataRequest().to_request(model)

    def insere_data(self, dto: DataRequest) -> DataRequest:
        model = DataModel().to_model(dto)
        with DBConnectionHandler() as db:
            try:
                db.session.add(model)
                db.session.commit()
                return DataRequest().to_request(model)
            except Exception as e:
                db.session.rollback()
                raise e
