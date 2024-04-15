package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.services.*;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class ValorController {

    private final ValorService service;

    @GetMapping
    public String obtemValores(){
        this.service.buscaValor();
        return "TESTE";
    }

}
