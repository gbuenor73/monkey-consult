package br.com.monkeyconsulting.services;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.models.PlanoModel;
import br.com.monkeyconsulting.repository.PlanoRepository;
import br.com.monkeyconsulting.utils.Utils;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class PlanoService {

    public final PlanoRepository jpa;

    public List<PlanoModel> buscaPlanos() {
        return this.jpa.findAll();
    }

    public PlanoModel buscaPorId(Integer idDieta) {
        Optional<PlanoModel> optional = this.jpa.findById(idDieta);
        return (PlanoModel) Utils.validaRetorno(optional);
    }

}
