from br.com.monkeyconsulting.infra.database.models.planos_model import PlanoModel


class PlanoDTO:
    def __init__(self, id_plano, dias_para_vencimento, dias_para_troca_da_dieta, descricao):
        self.id_plano = id_plano
        self.dias_para_vencimento = dias_para_vencimento
        self.dias_para_troca_da_dieta = dias_para_troca_da_dieta
        self.descricao = descricao

    @staticmethod
    def to_dto(model: PlanoModel):
        PlanoDTO.id_plano = model.id_plano
        PlanoDTO.dias_para_vencimento = model.dias_para_vencimento
        PlanoDTO.dias_para_troca_da_dieta = model.dias_para_troca_da_dieta
        PlanoDTO.descricao = model.descricao
        return PlanoDTO
