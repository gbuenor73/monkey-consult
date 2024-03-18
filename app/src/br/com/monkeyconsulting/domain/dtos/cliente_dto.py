from br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO
from src.br.com.monkeyconsulting.domain.dtos.dieta_treino_dto import DietaTreinoDTO
from src.br.com.monkeyconsulting.domain.dtos.plano_dto import PlanoDTO


class ClienteDTO:
    id = None
    nome = None
    telefone = None
    indicador_cliente_ativo = None
    plano = PlanoDTO()
    dieta = DietaTreinoDTO()
    data = DataDTO()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<ClienteDTO(id='{self.id}')>"
