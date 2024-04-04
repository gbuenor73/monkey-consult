import json

from com.monkeyconsulting.domain.dtos.plano_dto import PlanoDTO


class PlanoResponse:
    id_plano = None
    dias_para_vencimento = None
    dias_para_troca_da_dieta = None
    descricao = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"""
            id_plano: {self.id_plano},
            descricao: {self.descricao}
        """

    def to_json(self) -> json:
        return {
            'id_plano': self.id_plano if self.id_plano is not None else '',
            'dias_para_vencimento': self.dias_para_vencimento if self.dias_para_vencimento is not None else '',
            'dias_para_troca_da_dieta': self.dias_para_troca_da_dieta if self.dias_para_troca_da_dieta is not None else '',
            'descricao': self.descricao if self.descricao is not None else ''
        }

    def dto_to_response(self, dto: PlanoDTO):
        if dto is not None:
            self.id_plano = dto.id_plano
            self.dias_para_vencimento = dto.dias_para_vencimento
            self.dias_para_troca_da_dieta = dto.dias_para_troca_da_dieta
            self.descricao = dto.descricao
        return self
