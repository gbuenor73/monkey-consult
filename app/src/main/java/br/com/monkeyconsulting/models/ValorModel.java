package br.com.monkeyconsulting.models;

import jakarta.persistence.*;
import lombok.Data;

@Entity(name = "VALORES")
@Data
public class ValorModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_valor")
    private Integer idValor;

    @Column(name = "id_cliente")
    private Integer idCliente;

    @Column(name = "valor_bruto")
    private Float valorBruto;

    @Column(name = "valor_liquido")
    private Float valorLiquido;
}
