from src.br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel


class PlanoDTO:
    id_plano = None
    dias_para_vencimento = None
    dias_para_troca_da_dieta = None
    descricao = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<PlanoDTO(id_plano='{self.id_plano}')>"

    def to_dto(self, model: PlanoModel):
        self.id_plano = model.id_plano
        self.dias_para_vencimento = model.dias_para_vencimento
        self.dias_para_troca_da_dieta = model.dias_para_troca_da_dieta
        self.descricao = model.descricao
        return self

    def set_id(self, id_plano):
        self.id_plano = id_plano
        return self
