package br.com.monkeyconsulting.repository;

import br.com.monkeyconsulting.models.ClienteModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface ClienteRepository extends JpaRepository<ClienteModel, Integer> {
    Optional<ClienteModel> findByTelefone(Long telefone);
}
