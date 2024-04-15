package br.com.monkeyconsulting.models;

import jakarta.persistence.*;
import lombok.Data;


@Entity(name = "PLANOS")
@Data
public class PlanoModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_plano")
    private Integer id_plano;

    @Column(name = "dias_para_vencimento")
    private Integer dias_para_vencimento;

    @Column(name = "dias_para_troca_da_dieta")
    private Integer dias_para_troca_da_dieta;

    @Column(name = "descricao")
    private String descricao;

}
