package br.com.monkeyconsulting.repository;

import br.com.monkeyconsulting.models.DataModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DataRepository extends JpaRepository<DataModel, Integer> {
}
