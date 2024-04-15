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

    public void buscaDietasTreinos(){
        List<DietaTreinoModel> all = this.jpa.findAll();

        System.out.println();
    }

}
