from src.br.com.monkeyconsulting.domain.dtos.dieta_treino_dto import DietaTreinoDTO
from src.br.com.monkeyconsulting.domain.dtos.plano_dto import PlanoDTO
from src.br.com.monkeyconsulting.infra.database.models.cliente_model import ClienteModel


class ClienteDTO:
    plano = PlanoDTO(None, None, None, None)
    dieta = DietaTreinoDTO(None, None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def to_dto(req):
        ClienteDTO.id = req.id_cliente
        ClienteDTO.nome = req.nome
        ClienteDTO.telefone = req.telefone
        ClienteDTO.indicador_ativo = req.indicador_cliente_ativo
        ClienteDTO.plano = PlanoDTO.to_dto(req.plano)
        ClienteDTO.dieta = DietaTreinoDTO.to_dto(req.dieta)
        return ClienteDTO
