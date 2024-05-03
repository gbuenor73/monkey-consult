package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.services.DietaTreinoService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/treinos")
@RequiredArgsConstructor
public class DietaTreinoController {

    private final DietaTreinoService dietaTreinoService;

    @GetMapping
    public ResponseEntity obtemDietas() {
        return ResponseEntity.ok().body(this.dietaTreinoService.buscaDietasTreinos());
    }

}
