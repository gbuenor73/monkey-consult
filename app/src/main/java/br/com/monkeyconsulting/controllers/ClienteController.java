package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.services.ClienteService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
//@RequestMapping("/clientes")
@RequiredArgsConstructor
public class ClienteController {

    private final ClienteService clienteService;

    @GetMapping("/")
    public String obtemClientes(Model model){
        List<ClienteModel> clienteModels = this.clienteService.buscaClientes();
        model.addAttribute("clientes", clienteModels);

        return "index";
    }

    @GetMapping("/clientes")
    @ResponseBody
    public List<ClienteModel> obtemTodosClientes(){
        List<ClienteModel> clienteModels = this.clienteService.buscaClientes();

        return clienteModels;
    }

}
