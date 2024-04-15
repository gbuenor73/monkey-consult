package br.com.monkeyconsulting.models;

import jakarta.persistence.*;
import lombok.Data;


@Entity(name = "DIETAS_TREINOS")
@Data
public class DietaTreinoModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_dieta")
    private Integer idDieta;

    @Column(name = "descricao")
    private String descricao;
}
