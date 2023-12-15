import datetime


class ResponseCompletoDto:
    id_cliente: int
    nome: str
    telefone: str
    indicador_cliente_ativo: int
    plano: str
    dieta: str
    data_pagamento: datetime.date
    inicio_dieta_treino: datetime.date
    ultima_troca_dieta_treino: datetime.date
    proxima_troca_dieta_treino: datetime.date
    vencimento_plano: datetime.date

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_json(self):
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'indicador_cliente_ativo': self.indicador_cliente_ativo,
            'plano': self.plano,
            'dieta': self.dieta,
            'data_pagamento': self.data_pagamento,
            'inicio_dieta_treino': self.inicio_dieta_treino,
            'ultima_troca_dieta_treino': self.ultima_troca_dieta_treino,
            'proxima_troca_dieta_treino': self.proxima_troca_dieta_treino,
            'vencimento_plano': self.vencimento_plano
        }

    def __repr__(self):
        return f"<Response(nome='{self.nome}', indicador_cliente_ativo='{self.indicador_cliente_ativo}')>"