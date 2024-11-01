package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.models.DataModel;
import br.com.monkeyconsulting.models.ValorModel;
import br.com.monkeyconsulting.services.ClienteService;
import br.com.monkeyconsulting.services.DataService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.util.List;

@Controller
@RequestMapping("/datas")
@RequiredArgsConstructor
public class DataController {

    private final DataService dataService;
    private final ClienteService clienteService;

//    @GetMapping
//    public ResponseEntity obtemDatas() {
//        return ResponseEntity.ok(this.dataService.buscaDatas());
//    }

    @GetMapping("/detalhar/{id_cliente}")
    public String obtemPlanoPorId(Model model, @PathVariable("id_cliente") Integer idCliente) {
        ClienteModel clienteModel = this.clienteService.buscaClientePorId(idCliente);

        if (clienteModel.getDatasModel().isEmpty())
            clienteModel.setDatasModel(List.of(new DataModel()));

        if (clienteModel.getValoresModel().isEmpty())
            clienteModel.setValoresModel(List.of(new ValorModel()));

        model.addAttribute("cliente", clienteModel);
        return "informa_datas_cliente";
    }

    @PostMapping("/editar")
    public ResponseEntity informaDatas(
            @RequestParam("id_cliente") Integer idCliente,
            @RequestParam(value = "id_data", defaultValue = "") Integer idData,
            @RequestParam("data_pagamento_input") LocalDate dataPagamento,
            @RequestParam(value = "inicio_plano_input", defaultValue = "") LocalDate inicioPlano,
            @RequestParam(value = "id_valor", defaultValue = "") Integer idValor,
            @RequestParam("valor_bruto_input") Float valorBrutoString,
            @RequestParam("valor_liquido_input") Float valorLiquidoString,
            @RequestParam(value = "mesma_data_check", defaultValue = "") String mesmaDataString,
            @RequestParam(value = "iniciar_plano_check", defaultValue = "") String iniciarPlanoString) {

        ClienteModel clienteModel = this.clienteService.buscaClientePorId(idCliente);
        DataModel dataModel = new DataModel(idData, dataPagamento, null, inicioPlano, null, null, null, clienteModel);
        ValorModel valorModel = new ValorModel(idValor, valorBrutoString, valorLiquidoString, clienteModel);

        this.dataService.atualizarDatas(dataModel, valorModel, clienteModel, "on".equals(iniciarPlanoString), "on".equals(mesmaDataString));
        return ResponseEntity.ok().body("");
    }
}
