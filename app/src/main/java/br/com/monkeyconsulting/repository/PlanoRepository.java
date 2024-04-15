package br.com.monkeyconsulting.repository;

import br.com.monkeyconsulting.models.PlanoModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PlanoRepository extends JpaRepository<PlanoModel, Integer> {
}
