from com.monkeyconsulting.domain.dtos.valor_dto import ValorDTO
from com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from com.monkeyconsulting.infra.database.models.valor_model import ValorModel


class ValorRepository:

    def insere_valor(self, dto: ValorDTO) -> ValorDTO:
        model = ValorModel().to_model(dto)
        with DBConnectionHandler() as db:
            try:
                db.session.add(model)
                db.session.commit()
                return model.to_dto()
            except Exception as e:
                db.session.rollback()
                raise e

    def update_valor(self, dto: ValorDTO) -> ValorDTO:
        model = ValorModel().to_model(dto)
        with DBConnectionHandler() as db:
            try:
                db.session.merge(model)
                db.session.commit()
                return model.to_dto()
            except Exception as e:
                db.session.rollback()
                raise e

