package br.com.monkeyconsulting.models;

import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDate;


@Entity(name = "DATAS")
@Data
public class DataModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_data")
    private Integer idData;

    @Column(name = "id_cliente")
//    @OneToMany
    @JoinColumn(name = "id_cliente", nullable = false)
    private Integer idCliente;

    @Column(name = "data_pagamento")
    private LocalDate dataPagamento;

    @Column(name = "inicio_dieta_treino")
    private LocalDate inicioDietaTreino;

    @Column(name = "inicio_plano")
    private LocalDate inicioPlano;

    @Column(name = "ultima_troca_dieta_treino")
    private LocalDate ultimaTrocaDietaTreino;

    @Column(name = "proxima_troca_dieta_treino")
    private LocalDate proximaTrocaDietaTreino;

    @Column(name = "vencimento_plano")
    private LocalDate vencimentoPlano;

}
