package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.services.ClienteService;
import br.com.monkeyconsulting.services.DataService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

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
        model.addAttribute("cliente", clienteModel);
        return "informa_datas_cliente";
    }

    @PostMapping("/editar")
    public ResponseEntity informaDatas() {
        System.out.println();

        return ResponseEntity.ok().build();
    }

}
