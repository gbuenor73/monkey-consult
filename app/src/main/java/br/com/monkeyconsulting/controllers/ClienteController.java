package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.models.ValorModel;
import br.com.monkeyconsulting.services.ClienteService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import static java.util.Objects.nonNull;

@Controller("/clientes")
@RequiredArgsConstructor
public class ClienteController {

    private final ClienteService clienteService;

    @GetMapping("/")
    public String obtemClientes(Model model) {
        List<ClienteModel> clienteModels = this.clienteService.buscaClientes();
        model.addAttribute("clientes", clienteModels);
        return "index";
    }

    @GetMapping("/novo")
    public String novoCliente(Model model) {
        return "novo_cliente";
    }

    @PostMapping("/insere")
    public ResponseEntity<String> insereCliente(@RequestParam("nome") String nome,
                                        @RequestParam("telefone") Long telefone,
                                        @RequestParam("valor_bruto") Float valorBruto,
                                        @RequestParam("valor_liquido") Float valorLiquido) {

        var valorModel = new ValorModel();
        valorModel.setValorBruto(valorBruto);
        valorModel.setValorLiquido(valorLiquido);

        var cliente = new ClienteModel();
        cliente.setNome(nome);
        cliente.setTelefone(telefone);
        cliente.setIndicadorClienteAtivo(true);
        cliente.setValoresModel(List.of(valorModel));

        ClienteModel clienteModel = this.clienteService.buscaClientePorTelefone(cliente.getTelefone());

        if (nonNull(clienteModel) && nonNull(clienteModel.getTelefone()) && clienteModel.getTelefone().equals(telefone))
            throw new RuntimeException("Cliente ja existente!");

        this.clienteService.insereCliente(cliente);
        return ResponseEntity.ok().body("<script>window.close()</script>");
    }

    @GetMapping("/lista")
    @ResponseBody
    public List<ClienteModel> obtemTodosClientes() {
        List<ClienteModel> clienteModels = this.clienteService.buscaClientes();

        return clienteModels;
    }

    @DeleteMapping("/desativar")
    public void desativar(Model model){
        System.out.println(model);
    }

}
