package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.DietaTreinoModel;
import br.com.monkeyconsulting.repository.DietaTreinoRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class DietaTreinoService {

    public final DietaTreinoRepository jpa;

    public List<DietaTreinoModel> buscaDietasTreinos() {
        return this.jpa.findAll();
    }

}
