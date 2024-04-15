package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.services.*;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("/datas")
@RequiredArgsConstructor
public class DataController {

    private final DataService dataService;

    @GetMapping
    public String obtemDatas(){
        this.dataService.buscaDatas();
        return "TESTE";
    }

}
