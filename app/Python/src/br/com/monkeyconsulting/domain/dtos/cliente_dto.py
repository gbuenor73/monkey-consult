from br.com.monkeyconsulting.adapters.controllers.requests.cliente_req import ClienteRequest
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

    def from_model_to_dto(self, model):
        self.id = model.id_cliente
        self.nome = model.nome
        self.telefone = model.telefone
        self.indicador_cliente_ativo = model.indicador_cliente_ativo
        self.plano = PlanoDTO().to_dto(model.plano) if model.plano is not None else None
        self.dieta = DietaTreinoDTO().to_dto(model.dieta) if model.dieta is not None else None
        self.data = DataDTO().to_dto(model.data) if model.data is not None else None
        return self

    def from_req_to_dto(self, req: ClienteRequest):
        self.nome = req.get('nome')
        self.telefone = req.get('telefone')
        self.indicador_cliente_ativo = req.get('indicador_cliente_ativo')
        self.id = req.get('id_cliente')
        self.plano.id_plano = req.get('id_plano')
        self.dieta.id_dieta = req.get('id_dieta')
        self.data.id_data = req.get('id_data')
        return self
