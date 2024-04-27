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

    public void update(ValorModel valorModel) {
        this.insere(valorModel);
    }

    public void insere(ValorModel valorModel) {
        try {
            this.jpa.save(valorModel);
        } catch (Exception e) {
            throw new RuntimeException("Houve um erro ao inserir o valor, tente novamente: ".concat(e.getMessage()));
        }
    }
}
