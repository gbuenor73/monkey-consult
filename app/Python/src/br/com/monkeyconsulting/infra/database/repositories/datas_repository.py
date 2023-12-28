from src.br.com.monkeyconsulting.domain.dtos.completo_dto import CompletoDTO
from src.br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO
from src.br.com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from src.br.com.monkeyconsulting.infra.database.models.datas_model import DataModel


class DatasRepository:
    def busca_todas_datas(self):
        with DBConnectionHandler() as db:
            models = db.session.query(DataModel).all()
            if models is not None:
                return [DataDTO.to_dto(model) for model in models]
            return []

    def busca_datas_por_id(self, id):
        with DBConnectionHandler() as db:
            model = db.session.query(DataModel).filter_by(id_data=id).first()
            if model is not None:
                return DataDTO.to_dto(model)
            return None

    def retorno_completo(self):
        with DBConnectionHandler() as db:
            models = db.session.query(DataModel).all()
            return [CompletoDTO.to_dto(model) for model in models]

    def insere_data(self, dto: DataDTO) -> DataDTO:
        model = DataModel().to_model(dto)
        with DBConnectionHandler() as db:
            try:
                db.session.add(model)
                db.session.commit()
                return DataDTO.to_dto(model)
            except Exception as e:
                db.session.rollback()
                raise e
