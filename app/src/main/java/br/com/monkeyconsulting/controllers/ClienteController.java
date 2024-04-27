package br.com.monkeyconsulting.controllers;

import br.com.monkeyconsulting.models.ClienteModel;
import br.com.monkeyconsulting.models.DietaTreinoModel;
import br.com.monkeyconsulting.models.PlanoModel;
import br.com.monkeyconsulting.models.ValorModel;
import br.com.monkeyconsulting.services.ClienteService;
import br.com.monkeyconsulting.services.DietaTreinoService;
import br.com.monkeyconsulting.services.PlanoService;
import br.com.monkeyconsulting.services.ValorService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import static java.util.Objects.isNull;
import static java.util.Objects.nonNull;


@Controller
@RequiredArgsConstructor
public class ClienteController {

    private final ClienteService clienteService;
    private final ValorService valorService;
    private final PlanoService planoService;
    private final DietaTreinoService dietaTreinoService;

    @GetMapping
    public String obtemClientes(Model model) {
        List<ClienteModel> clienteModels = this.clienteService.buscaClientes();
        model.addAttribute("clientes", clienteModels);
        return "index";
    }

    @GetMapping("/novo")
    public String novoCliente(Model model) {
        return "novo_cliente";
    }

    @GetMapping("/detalhar/{id_cliente}")
    public String detalhaCliente(Model model, @PathVariable("id_cliente") Integer idCliente) {

        ClienteModel clienteModel = this.clienteService.buscaClientePorId(idCliente);
        List<PlanoModel> listaPlanos = this.planoService.buscaPlanos();
        List<DietaTreinoModel> listaTreinos = this.dietaTreinoService.buscaDietasTreinos();

        model.addAttribute("cliente", clienteModel);
        model.addAttribute("planos", listaPlanos);
        model.addAttribute("dietas", listaTreinos);

        return "edita_cliente";
    }

    @PostMapping("/editar")
    public ResponseEntity editar(@RequestParam("id_cliente") Integer idCliente,
                                 @RequestParam("indicador_cliente_ativo") String indicador,
                                 @RequestParam("nome") String nome,
                                 @RequestParam("telefone") Long telefone,
                                 @RequestParam("plano") Integer idPlano,
                                 @RequestParam("dieta") Integer idDieta) {

        this.clienteService.editaCliente(idCliente, indicador, nome, telefone, idPlano, idDieta);
        return ResponseEntity.ok().body("<script>window.close()</script>");
    }

    @PostMapping("/insere")
    public ResponseEntity<String> insereCliente(@RequestParam("nome") String nome,
                                                @RequestParam("telefone") Long telefone,
                                                @RequestParam("valor_bruto") Float valorBruto,
                                                @RequestParam("valor_liquido") Float valorLiquido) {

        var cliente = new ClienteModel();
        cliente.setNome(nome);
        cliente.setTelefone(telefone);
        cliente.setIndicadorClienteAtivo(true);


//        valorModel.setValorBruto(valorBruto);
//        valorModel.setValorLiquido(valorLiquido);


        ClienteModel clienteModel = this.clienteService.buscaClientePorTelefone(cliente.getTelefone());

        if (nonNull(clienteModel) && nonNull(clienteModel.getTelefone()) && clienteModel.getTelefone().equals(telefone))
            throw new RuntimeException("Cliente ja existente!");

        this.clienteService.insere(cliente);

        if (nonNull(valorBruto) || nonNull(valorLiquido)) {
            var valorModel = new ValorModel();

            if (nonNull(valorBruto))
                valorModel.setValorBruto(valorBruto);

            if (nonNull(valorLiquido))
                valorModel.setValorLiquido(valorLiquido);

            valorModel.setClientesModel(cliente);
            cliente.setValoresModel(List.of(valorModel));

            this.valorService.insere(valorModel);
        } else {
            throw new RuntimeException("Valores inválidoos!");
        }
        return ResponseEntity.ok().body("<script>window.close()</script>");
    }

    @DeleteMapping("/desativar/{id_cliente}")
    public ResponseEntity desativar(@PathVariable("id_cliente") Integer idCliente) {

        ClienteModel clienteModel = this.clienteService.buscaClientePorId(idCliente);

        if (isNull(clienteModel))
            throw new RuntimeException("Cliente Não encontrado");

        this.clienteService.cancelarCliente(clienteModel.getIdCliente());
        return ResponseEntity.ok("Sucessp");
    }


    @GetMapping("/lista")
    @ResponseBody
    public List<ClienteModel> obtemTodosClientes() {
        List<ClienteModel> clienteModels = this.clienteService.buscaClientes();

        return clienteModels;
    }

}
