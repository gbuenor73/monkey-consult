package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.services.*;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("/treinos")
@RequiredArgsConstructor
public class DietaTreinoController {

    private final DietaTreinoService dietaTreinoService;

    @GetMapping
    public String obtemDietas(){
        this.dietaTreinoService.buscaDietasTreinos();
        return "TESTE";
    }

}
