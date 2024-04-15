package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.services.PlanoService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("/planos")
@RequiredArgsConstructor
public class PlanosController {

    private final PlanoService service;

    @GetMapping
    public String obtemPlanos(){
        this.service.buscaPlanos();
        return "TESTE";
    }

}
