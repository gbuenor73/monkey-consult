package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.services.ClienteService;
import br.com.monkeyconsulting.services.PlanoService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/planos")
@RequiredArgsConstructor
public class PlanosController {

    private final PlanoService service;
    private final ClienteService clienteService;

//    @GetMapping
//    @ResponseBody
//    public List<PlanoModel> obtemPlanos() {
//        return this.service.buscaPlanos();
//    }



}
