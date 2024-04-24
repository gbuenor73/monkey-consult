package br.com.monkeyconsulting;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ApplicationStart {

    private static final Logger log = LoggerFactory.getLogger(ApplicationStart.class);

    public static void main(String[] args) {
        log.info("Iniciando Sistema");
        SpringApplication.run(ApplicationStart.class, args);
    }

}
