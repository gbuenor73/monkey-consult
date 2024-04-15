package br.com.monkeyconsulting.repository;

import br.com.monkeyconsulting.models.DataModel;
import br.com.monkeyconsulting.models.DietaTreinoModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DietaTreinoRepository extends JpaRepository<DietaTreinoModel, Integer> {
}
