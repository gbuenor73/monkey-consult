package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.ValorModel;
import br.com.monkeyconsulting.repository.ValorRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ValorService {

    public final ValorRepository jpa;

    public void buscaValor() {
        List<ValorModel> all = this.jpa.findAll();

        System.out.println();
    }

}
