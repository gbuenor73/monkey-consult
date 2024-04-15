from com.monkeyconsulting.infra.database.config_db import DBConnectionHandler
from com.monkeyconsulting.infra.database.models import ClienteModel


# from com.monkeyconsulting.infra.database.models import ClienteModel
# from com.monkeyconsulting.infra.database.models import ValorModel


# from com.monkeyconsulting.infra.database.models.valor_model import ValorModel


class CompletoRepository:

    def busca_completa(self):
        with DBConnectionHandler() as db:
            clientes_model = db.session.query("ClienteModel").filter_by(indicador_cliente_ativo=True).all()
            valores_model = db.session.query("ValorModel")

            teste = db.session.query("ClienteModel") \
                .join('VALORES') \
                .filter(
                ClienteModel.indicador_cliente_ativo == True
            )

            clientes_dto = [model.to_dto() for model in clientes_model]
            valores_dto = [model.to_dto() for model in valores_model]

            print()

        # for cliente in clientes_dto:
        #     for valor in valores_dto:
        #         if valor.id

    # return []
