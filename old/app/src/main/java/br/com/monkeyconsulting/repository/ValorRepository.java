package br.com.monkeyconsulting.repository;

import br.com.monkeyconsulting.models.ValorModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ValorRepository extends JpaRepository<ValorModel, Integer> {
}
