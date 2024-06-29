package br.com.monkeyconsulting.repository;

import br.com.monkeyconsulting.models.ClienteModel;
import jakarta.transaction.Transactional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ClienteRepository extends JpaRepository<ClienteModel, Integer> {

    Optional<ClienteModel> findByTelefone(Long telefone);

    @Transactional
    @Modifying
    @Query("UPDATE CLIENTES c SET c.indicadorClienteAtivo = false WHERE c.idCliente = :idCliente")
    void desativarCliente(Integer idCliente);

    List<ClienteModel> findByIndicadorClienteAtivo(boolean indicadorClienteAtivo);

}
