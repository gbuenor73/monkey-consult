package br.com.monkeyconsulting.models;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;


@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity(name = "DATAS")
public class DataModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_data")
    @JsonProperty("id_data")
    private Integer idData;

    @Column(name = "data_pagamento")
    @JsonProperty("data_pagamento")
    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate dataPagamento;

    @Column(name = "inicio_dieta_treino")
    @JsonProperty("inicio_dieta_treino")
    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate inicioDietaTreino;

    @Column(name = "inicio_plano")
    @JsonProperty("inicio_plano")
    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate inicioPlano;

    @Column(name = "ultima_troca_dieta_treino")
    @JsonProperty("ultima_troca_dieta_treino")
    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate ultimaTrocaDietaTreino;

    @Column(name = "proxima_troca_dieta_treino")
    @JsonProperty("proxima_troca_dieta_treino")
    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate proximaTrocaDietaTreino;

    @Column(name = "vencimento_plano")
    @JsonProperty("vencimento_plano")
    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate vencimentoPlano;

    @ManyToOne
    @JoinColumn(name = "id_cliente")
    @JsonBackReference
    @JsonProperty("id_cliente")
    private ClienteModel clientesModel;

    @Override
    public String toString() {
        return "DataModel(" +
                "idData=" + idData +
                ", dataPagamento=" + dataPagamento +
                ", inicioDietaTreino=" + inicioDietaTreino +
                ", inicioPlano=" + inicioPlano +
                ", ultimaTrocaDietaTreino=" + ultimaTrocaDietaTreino +
                ", proximaTrocaDietaTreino=" + proximaTrocaDietaTreino +
                ", vencimentoPlano=" + vencimentoPlano +
                ')';
    }

}
