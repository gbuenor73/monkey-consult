package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.DataModel;
import br.com.monkeyconsulting.repository.DataRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class DataService {

    public final DataRepository jpa;

    public void buscaDatas(){
        List<DataModel> all = this.jpa.findAll();

        System.out.println();
    }

}
