package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.PlanoModel;
import br.com.monkeyconsulting.repository.PlanoRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class PlanoService {

    public final PlanoRepository jpa;

    public List<PlanoModel> buscaPlanos() {
        return this.jpa.findAll();
    }

}
