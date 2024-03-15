USE monkey_consulting;

CREATE TABLE IF NOT EXISTS PLANOS (
    id_plano INT AUTO_INCREMENT PRIMARY KEY, dias_para_vencimento INT, dias_para_troca_da_dieta INT, descricao TEXT
);

CREATE TABLE IF NOT EXISTS DIETAS_TREINOS (
    id_dieta INT AUTO_INCREMENT PRIMARY KEY, descricao TEXT
);

CREATE TABLE IF NOT EXISTS DATAS (
    id_data INT AUTO_INCREMENT PRIMARY KEY, data_pagamento DATE, inicio_dieta_treino DATE, inicio_plano DATE, ultima_troca_dieta_treino DATE, proxima_troca_dieta_treino DATE, vencimento_plano DATE
);

CREATE TABLE IF NOT EXISTS CLIENTES (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY, id_plano INT, id_dieta INT, id_data INT, nome VARCHAR(200), telefone VARCHAR(20), indicador_cliente_ativo BOOLEAN, FOREIGN KEY (id_plano) REFERENCES PLANOS (id_plano), FOREIGN KEY (id_dieta) REFERENCES DIETAS_TREINOS (id_dieta), FOREIGN KEY (id_data) REFERENCES DATAS (id_data)
);

ALTER TABLE CLIENTES
ADD CONSTRAINT fk_clientes_planos FOREIGN KEY (id_plano) REFERENCES PLANOS (id_plano);

ALTER TABLE CLIENTES
ADD CONSTRAINT fk_clientes_dietas FOREIGN KEY (id_dieta) REFERENCES DIETAS_TREINOS (id_dieta);

ALTER TABLE CLIENTES
ADD CONSTRAINT fk_clientes_datas FOREIGN KEY (id_data) REFERENCES DATAS (id_data);

INSERT INTO
    PLANOS (
        dias_para_vencimento, dias_para_troca_da_dieta, descricao
    )
VALUES (NULL, NULL, 'Sem Plano'),
    (
        30, 30, 'Plano de 30 dias com troca a cada 30 dias'
    ),
    (
        90, 45, 'Plano de 90 dias com troca a cada 45 dias'
    ),
    (
        120, 60, 'Plano de 120 dias com troca a cada 60 dias'
    ),
    (
        180, 60, 'Plano de 180 dias com troca a cada 60 dias'
    ),
    (
        360, 60, 'Plano de 360 dias com troca a cada 60 dias'
    );

INSERT INTO
    DIETAS_TREINOS (descricao)
VALUES ('Sem treino'),
    ('Perda de peso'),
    ('Ganho de massa muscular');

INSERT INTO
    DATAS (
        data_pagamento, inicio_dieta_treino, inicio_plano, ultima_troca_dieta_treino, proxima_troca_dieta_treino, vencimento_plano
    )
VALUES (
        NOW(), NOW(), NOW(), NOW(), NOW(), NOW()
    );

INSERT INTO
    CLIENTES (
        nome, telefone, indicador_cliente_ativo, id_plano, id_dieta, id_data
    )
VALUES (
        'gabriel', '11951269909', true, 1, 2, 1
    );

SELECT *
FROM
    `CLIENTES` c
    JOIN `PLANOS` p ON c.id_plano = p.id_plano
    JOIN `DIETAS_TREINOS` dt ON c.id_dieta = dt.id_dieta
    JOIN `DATAS` ds ON c.id_data = ds.id_data;

SELECT * FROM `CLIENTES` c ORDER BY `id_cliente` DESC