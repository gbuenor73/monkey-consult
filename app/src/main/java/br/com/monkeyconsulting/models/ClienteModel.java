package br.com.monkeyconsulting.models;

import com.fasterxml.jackson.annotation.JsonIdentityInfo;
import com.fasterxml.jackson.annotation.JsonManagedReference;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.ObjectIdGenerators;
import jakarta.persistence.*;
import lombok.Data;

import java.util.List;


@Entity(name = "CLIENTES")
@JsonIdentityInfo(generator = ObjectIdGenerators.PropertyGenerator.class, property = "id_cliente")
@Data
public class ClienteModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_cliente")
    private Integer id_cliente;
    
    @Column(name = "nome")
    private String nome;
    
    @Column(name = "telefone")
    private Long telefone;
    
    @Column(name = "indicador_cliente_ativo")
    private Boolean indicador_cliente_ativo;

    @ManyToOne
    @JsonProperty("plano")
    @JoinColumn(name = "id_plano")
    private PlanoModel  planoModel;

    @ManyToOne
    @JsonProperty("dieta")
    @JoinColumn(name = "id_dieta")
    private DietaTreinoModel dietaTreinoModel;

    @JsonProperty("valores")
    @OneToMany(mappedBy = "clientesModel")
    @JsonManagedReference
    private List<ValorModel> valoresModel;

    @JsonProperty("datas")
    @OneToMany(mappedBy = "clientesModel")
    @JsonManagedReference
    private List<DataModel> datasModel;

}
