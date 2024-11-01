package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.DietaTreinoModel;
import br.com.monkeyconsulting.repository.DietaTreinoRepository;
import br.com.monkeyconsulting.utils.Utils;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class DietaTreinoService {

    public final DietaTreinoRepository jpa;

    public List<DietaTreinoModel> buscaDietasTreinos() {
        return this.jpa.findAll();
    }

    public DietaTreinoModel buscaPorId(Integer id) {
        Optional<DietaTreinoModel> optional = this.jpa.findById(id);
        return (DietaTreinoModel) Utils.validaRetorno(optional);
    }

}
