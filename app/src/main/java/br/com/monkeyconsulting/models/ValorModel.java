package br.com.monkeyconsulting.models;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity(name = "VALORES")
public class ValorModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_valor")
    @JsonProperty("id_valor")
    private Integer idValor;

    @Column(name = "valor_bruto")
    @JsonProperty("valor_bruto")
    private Float valorBruto;

    @Column(name = "valor_liquido")
    @JsonProperty("valor_liquido")
    private Float valorLiquido;

    @ManyToOne
    @JoinColumn(name = "id_cliente")
    @JsonBackReference
    @JsonProperty("id_cliente")
    private ClienteModel clientesModel;

    @Override
    public String toString() {
        return "ValorModel{" +
                "idValor=" + idValor +
                ", valorBruto=" + valorBruto +
                ", valorLiquido=" + valorLiquido +
                '}';
    }
}
