package br.com.monkeyconsulting.models;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;
import lombok.Data;


@Entity(name = "PLANOS")
@Data
public class PlanoModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_plano")
    @JsonProperty("id_plano")
    private Integer idPlano;

    @Column(name = "dias_para_vencimento")
    @JsonProperty("dias_para_vencimento")
    private Integer diasParaVencimento;

    @Column(name = "dias_para_troca_da_dieta")
    @JsonProperty("dias_para_troca_da_dieta")
    private Integer diasParaTrocaDaDieta;

    @Column(name = "descricao")
    @JsonProperty("descricao")
    private String descricao;

}
