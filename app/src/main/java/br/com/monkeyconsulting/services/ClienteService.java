package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.models.DietaTreinoModel;
import br.com.monkeyconsulting.models.PlanoModel;
import br.com.monkeyconsulting.repository.ClienteRepository;
import br.com.monkeyconsulting.utils.Utils;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class ClienteService {

    private final ClienteRepository jpa;
    private final DataService dataService;
    private final DietaTreinoService dietaTreinoService;
    private final PlanoService planoService;


    public List<ClienteModel> buscaClientes() {
        var clientes = this.jpa.findByIndicadorClienteAtivo(true);
        return clientes;
    }

    public ClienteModel buscaClientePorId(Integer idCliente) {
        Optional<ClienteModel> optional = this.jpa.findById(idCliente);
        return (ClienteModel) Utils.validaRetorno(optional);
    }

    public ClienteModel buscaClientePorTelefone(Long telefone) {
        Optional<ClienteModel> optional = this.jpa.findByTelefone(telefone);
        return (ClienteModel) Utils.validaRetorno(optional);
    }

    public ClienteModel insere(ClienteModel clienteModel) {
        try {
            ClienteModel save = this.jpa.save(clienteModel);
            return save;
        } catch (Exception e){
            throw new RuntimeException("Houve um erro ao inserir o cliente, tente novamente: ".concat(e.getMessage()));
        }
    }

    public void cancelarCliente(Integer idCliente) {
        try {
            this.jpa.desativarCliente(idCliente);
        } catch (Exception e) {
            throw new RuntimeException("Houve um erro ao atualizar o cliente: "
                    .concat(idCliente.toString()
                            .concat(". Erro: ")
                            .concat(e.getMessage())));
        }
    }

    public ClienteModel editaCliente(Integer idCliente, String indicadorClienteAtivo, String nome, Long telefone, Integer idPlano, Integer idDieta) {
        ClienteModel clienteModel = this.buscaClientePorId(idCliente);
        PlanoModel planoModel = this.planoService.buscaPorId(idPlano);
        DietaTreinoModel dietaTreinoModel = this.dietaTreinoService.buscaPorId(idDieta);

        clienteModel.setNome(nome);
        clienteModel.setTelefone(telefone);
        clienteModel.setIndicadorClienteAtivo(Boolean.parseBoolean(indicadorClienteAtivo));
        clienteModel.setPlanoModel(planoModel);
        clienteModel.setDietaTreinoModel(dietaTreinoModel);

        try {
            return this.jpa.save(clienteModel);
        } catch (Exception e){
            throw new RuntimeException("Houve um erro ao inserir o cliente, tente novamente: ".concat(e.getMessage()));
        }
    }
}
