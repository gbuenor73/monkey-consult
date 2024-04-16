package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.repository.ClienteRepository;
import br.com.monkeyconsulting.repository.DataRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ClienteService {

    public final ClienteRepository jpa;
    private final DataRepository dataRepository;

    public List<ClienteModel> buscaClientes(){
         var clientes = this.jpa.findAll();

        for (ClienteModel cliente : clientes)
            cliente.setDatasModel(List.of(this.dataRepository.findLastDataByClientesModelIdCliente(cliente.getId_cliente())));

         return clientes;
    }

}
