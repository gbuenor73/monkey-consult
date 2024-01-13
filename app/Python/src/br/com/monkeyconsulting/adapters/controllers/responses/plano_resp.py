import json

from src.br.com.monkeyconsulting.domain.dtos.plano_dto import PlanoDTO


class PlanoResponse:
    def __init__(self, dto: PlanoDTO):
        self.id_plano = dto.id_plano
        self.dias_para_vencimento = dto.dias_para_vencimento
        self.dias_para_troca_da_dieta = dto.dias_para_troca_da_dieta
        self.descricao = dto.descricao

    def __repr__(self):
        return f"""
            id_plano: {self.id_plano},
            descricao: {self.descricao}
        """

    def to_json(self) -> json:
        return {
            'id_plano': self.id_plano,
            'dias_para_vencimento': self.dias_para_vencimento,
            'dias_para_troca_da_dieta': self.dias_para_troca_da_dieta,
            'descricao': self.descricao
        }
