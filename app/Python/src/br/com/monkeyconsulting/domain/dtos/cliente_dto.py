from br.com.monkeyconsulting.domain.dtos.data_dto import DataDTO
from src.br.com.monkeyconsulting.domain.dtos.dieta_treino_dto import DietaTreinoDTO
from src.br.com.monkeyconsulting.domain.dtos.plano_dto import PlanoDTO


class ClienteDTO:
    id = None
    nome = None
    telefone = None
    indicador_ativo = None
    plano = PlanoDTO(None, None, None, None)
    dieta = DietaTreinoDTO(None, None)
    data = DataDTO(None, None, None, None, None, None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<ClienteDTO(id='{self.id}')>"

    # @staticmethod
    def to_dto(self, req):
        self.id = req.id_cliente
        self.nome = req.nome
        self.telefone = req.telefone
        self.indicador_ativo = req.indicador_cliente_ativo
        self.plano = PlanoDTO.to_dto(req.plano) if req.plano is not None else None
        self.dieta = DietaTreinoDTO.to_dto(req.dieta) if req.dieta is not None else None
        self.data = DataDTO.to_dto(req.data) if req.data is not None else None
        return self
