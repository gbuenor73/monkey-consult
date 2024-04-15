package br.com.monkeyconsulting.models;

import jakarta.persistence.*;
import lombok.Data;


@Entity(name = "CLIENTES")
@Data
public class ClienteModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_cliente")
    private Integer id_cliente;
    
    @Column(name = "nome")
    private String nome;
    
    @Column(name = "telefone")
    private Integer telefone;
    
    @Column(name = "indicador_cliente_ativo")
    private Boolean indicador_cliente_ativo;
    
    @Column(name = "id_plano")
    private Integer id_plano;
    
    @Column(name = "id_dieta")
    private Integer id_dieta;
    
}
