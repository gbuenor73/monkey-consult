package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.repository.ClienteRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ClienteService {

    public final ClienteRepository jpa;

    public List<ClienteModel> buscaClientes(){
         return this.jpa.findAll();
    }

}
