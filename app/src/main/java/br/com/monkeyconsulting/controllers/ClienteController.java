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
import java.util.Map;

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
    public String obtemClientes(@RequestParam(value = "order", required = false) String order,
                                @RequestParam(value = "ascending", required = false) Boolean ascendig,
                                Model model) {
        List<ClienteModel> clienteModels = this.clienteService.buscaClientes(order, ascendig);
        model.addAttribute("clientes", clienteModels);
        return "index";
    }

    @GetMapping("/novo")
    public String novoCliente(Model model) {
        return "novo_cliente";
    }

    @GetMapping("/detalhar/{id_cliente}")
    public String detalhaCliente(@PathVariable("id_cliente") Integer idCliente, Model model) {

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

        ClienteModel clienteModel = this.clienteService.buscaClientePorTelefone(cliente.getTelefone());

        if (nonNull(clienteModel) && nonNull(clienteModel.getTelefone()) && clienteModel.getTelefone().equals(telefone)) {
            ResponseEntity<String> body = ResponseEntity.badRequest().body(Map.of("error_message", "Telefone ja cadastrado!",
                    "indicador_cliente_ativo", clienteModel.getIndicadorClienteAtivo(),
                    "id_cliente", clienteModel.getIdCliente()).toString());
            return body;
        }

        cliente.setIndicadorClienteAtivo(true);
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
//            throw new RuntimeException("Valores inválidos!");
            return ResponseEntity.badRequest().body("Valores inválidos");
        }
        return ResponseEntity.ok().build();
    }

    @DeleteMapping("/desativar/{id_cliente}")
    public ResponseEntity desativar(@PathVariable("id_cliente") Integer idCliente) {

        ClienteModel clienteModel = this.clienteService.buscaClientePorId(idCliente);

        if (isNull(clienteModel))
            throw new RuntimeException("Cliente Não encontrado");

        this.clienteService.cancelarCliente(clienteModel.getIdCliente());
        return ResponseEntity.ok("Sucesso");
    }

    @PostMapping("/reativar-cliente")
    public ResponseEntity reativar(@RequestParam("id_cliente") Integer idCliente) {
        try {
            ClienteModel clienteModel = this.clienteService.buscaClientePorId(idCliente);
            clienteModel.setIndicadorClienteAtivo(true);

            this.clienteService.insere(clienteModel);
            return ResponseEntity.ok("<script>window.close()</script>");
        } catch (Exception e) {
            return ResponseEntity.badRequest().build();
        }
    }

    @GetMapping("/lista")
    @ResponseBody
    public List<ClienteModel> obtemTodosClientes() {
        List<ClienteModel> clienteModels = this.clienteService.buscaClientes(null, null);
        return clienteModels;
    }

    @GetMapping("cliente/{id_cliente}")
    @ResponseBody
    public ResponseEntity buscaPorId(@PathVariable("id_cliente") Integer id, Model model) {
        ClienteModel clienteModel = this.clienteService.buscaClientePorId(id);
        model.addAttribute("cliente", clienteModel);
        return ResponseEntity.ok().build();
    }

}
