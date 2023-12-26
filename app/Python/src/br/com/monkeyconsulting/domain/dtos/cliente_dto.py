from br.com.monkeyconsulting.domain.dtos.dieta_treino_dto import DietaTreinoDTO
from br.com.monkeyconsulting.domain.dtos.plano_dto import PlanoDTO


class ClienteDTO:
    plano = PlanoDTO(None, None, None, None)
    dieta = DietaTreinoDTO(None, None)

    def __init__(self, id, nome, telefone, indicador_ativo, plano, dieta):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.indicador_ativo = indicador_ativo
        self.plano = plano
        self.dieta = dieta

    @staticmethod
    def to_dto(req):
        ClienteDTO.id = req.id_cliente
        ClienteDTO.nome = req.nome
        ClienteDTO.telefone = req.telefone
        ClienteDTO.indicador_ativo = req.indicador_cliente_ativo
        ClienteDTO.plano = PlanoDTO.to_dto(req.plano)
        ClienteDTO.dieta = DietaTreinoDTO.to_dto(req.dieta)
        return ClienteDTO
