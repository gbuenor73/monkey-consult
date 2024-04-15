package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.services.DataService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/datas")
@RequiredArgsConstructor
public class DataController {

    private final DataService dataService;

    @GetMapping
    public ResponseEntity obtemDatas(){
        return ResponseEntity.ok(this.dataService.buscaDatas());
    }

}
