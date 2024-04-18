package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.models.PlanoModel;
import br.com.monkeyconsulting.services.PlanoService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/planos")
@RequiredArgsConstructor
public class PlanosController {

    private final PlanoService service;

    @GetMapping
    public List<PlanoModel> obtemPlanos() {
        return this.service.buscaPlanos();
    }

}
