package br.com.monkeyconsulting.models;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;
import lombok.Data;


@Entity(name = "DIETAS_TREINOS")
@Data
public class DietaTreinoModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_dieta")
    @JsonProperty("id_dieta")
    private Integer idDieta;

    @Column(name = "descricao")
    @JsonProperty("descricao")
    private String descricao;
}
