package br.com.monkeyconsulting.models;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDate;


@Entity(name = "DATAS")
@Data
public class DataModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_data")
    @JsonProperty("id_data")
    private Integer idData;

    @Column(name = "data_pagamento")
    @JsonProperty("data_pagamento")
    private LocalDate dataPagamento;

    @Column(name = "inicio_dieta_treino")
    @JsonProperty("inicio_dieta_treino")
    private LocalDate inicioDietaTreino;

    @Column(name = "inicio_plano")
    @JsonProperty("inicio_plano")
    private LocalDate inicioPlano;

    @Column(name = "ultima_troca_dieta_treino")
    @JsonProperty("ultima_troca_dieta_treino")
    private LocalDate ultimaTrocaDietaTreino;

    @Column(name = "proxima_troca_dieta_treino")
    @JsonProperty("proxima_troca_dieta_treino")
    private LocalDate proximaTrocaDietaTreino;

    @Column(name = "vencimento_plano")
    @JsonProperty("vencimento_plano")
    private LocalDate vencimentoPlano;

    @ManyToOne
    @JoinColumn(name = "id_cliente")
    @JsonBackReference
    @JsonProperty("id_cliente")
    private ClienteModel clientesModel;
}
