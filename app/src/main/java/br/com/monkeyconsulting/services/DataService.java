package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.models.DataModel;
import br.com.monkeyconsulting.models.ValorModel;
import br.com.monkeyconsulting.repository.DataRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class DataService {

    public final DataRepository jpa;
    public final ValorService valorService;

    public List<DataModel> buscaDatas() {
        return this.jpa.findAll();
    }

    public DataModel buscaUltimaDataPeloCliente(ClienteModel cliente) {
        return this.jpa.findLastByClientesModel(cliente);
    }

    public void atualizarDatas(DataModel dataModel, ValorModel valorModel, ClienteModel clienteModel,Boolean iniciarPlano, Boolean mesmaData) {

        if (iniciarPlano){
            dataModel.setVencimentoPlano(dataModel.getInicioPlano().plusDays(clienteModel.getPlanoModel().getDiasParaVencimento()));

            dataModel.setInicioDietaTreino(dataModel.getInicioPlano());
            dataModel.setProximaTrocaDietaTreino(dataModel.getInicioDietaTreino().plusDays(clienteModel.getPlanoModel().getDiasParaTrocaDaDieta()));
        }

        try {
            this.jpa.save(dataModel);
        } catch (Exception e) {
            throw new RuntimeException("Houve um erro ao inserir o data, tente novamente: ".concat(e.getMessage()));
        }

        this.valorService.update(valorModel);
    }
}
