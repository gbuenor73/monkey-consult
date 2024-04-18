package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.repository.ClienteRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class ClienteService {

    private final ClienteRepository jpa;
    private final DataService dataService;


    public List<ClienteModel> buscaClientes() {
        var clientes = this.jpa.findAll();

        return clientes;
    }

    public ClienteModel buscaClientePorId(Integer idCliente) {

        Optional<ClienteModel> optional = this.jpa.findById(idCliente);

        return (ClienteModel) validaRetorno(optional);
    }

    public ClienteModel buscaClientePorTelefone(Long telefone) {

        Optional<ClienteModel> optional = this.jpa.findByTelefone(telefone);
        return (ClienteModel) validaRetorno(optional);
    }

    private <T> Object validaRetorno(Optional<T> optional) {
        if (optional.isPresent())
            return optional.orElseThrow(() -> new RuntimeException("Houve um problema ao obter o Cliente")  );
        return null;
    }

    public ClienteModel insereCliente(ClienteModel clienteModel) {
        try {
            ClienteModel save = this.jpa.save(clienteModel);
            return save;
        } catch (Exception e){
            throw new RuntimeException("Houve um erro ao inserir o cliente, tente novamente: ".concat(e.getMessage()));
        }
    }
}
