CREATE DATABASE IF NOT EXISTs monkey_consulting;

USE monkey_consulting;

CREATE TABLE IF NOT EXISTS PLANOS (
    id_plano INT AUTO_INCREMENT PRIMARY KEY, dias_para_vencimento INT, dias_para_troca_da_dieta INT, descricao TEXT
);

CREATE TABLE IF NOT EXISTS DIETAS_TREINOS (
    id_dieta INT AUTO_INCREMENT PRIMARY KEY, descricao TEXT
);

CREATE TABLE IF NOT EXISTS CLIENTES (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(200), 
    telefone VARCHAR(20) UNIQUE, 
    indicador_cliente_ativo BOOLEAN,
    id_plano INT,
    id_dieta INT,
    FOREIGN KEY (id_plano) REFERENCES PLANOS (id_plano),
    FOREIGN KEY (id_dieta) REFERENCES DIETAS_TREINOS (id_dieta)
);

CREATE TABLE IF NOT EXISTS DATAS (
    id_data INT AUTO_INCREMENT PRIMARY KEY, data_pagamento DATE, inicio_dieta_treino DATE, inicio_plano DATE, ultima_troca_dieta_treino DATE, proxima_troca_dieta_treino DATE, vencimento_plano DATE,
    id_cliente INT, FOREIGN KEY (id_cliente) REFERENCES CLIENTES (id_cliente)
);

CREATE TABLE IF NOT EXISTS VALORES (
    id_valor INT AUTO_INCREMENT PRIMARY KEY, valor_liquido DECIMAL(10,2), valor_bruto DECIMAL(10,2),
    id_cliente INT, FOREIGN KEY (id_cliente) REFERENCES CLIENTES (id_cliente)
);


ALTER TABLE CLIENTES
ADD CONSTRAINT fk_clientes_planos FOREIGN KEY (id_plano) REFERENCES PLANOS (id_plano);

ALTER TABLE CLIENTES
ADD CONSTRAINT fk_clientes_dietas FOREIGN KEY (id_dieta) REFERENCES DIETAS_TREINOS (id_dieta);

ALTER TABLE DATAS
ADD CONSTRAINT fk_datas_clientes FOREIGN KEY (id_cliente) REFERENCES CLIENTES (id_cliente);

ALTER TABLE VALORES
ADD CONSTRAINT fk_valores_clientes FOREIGN KEY (id_cliente) REFERENCES CLIENTES (id_cliente);

INSERT INTO PLANOS
    (dias_para_vencimento, dias_para_troca_da_dieta, descricao)
VALUES (NULL, NULL, 'Sem Plano'),
    (30, 30, 'Plano de 30 dias com troca a cada 30 dias'),
    (90, 45, 'Plano de 90 dias com troca a cada 45 dias'),
    (120, 60, 'Plano de 120 dias com troca a cada 60 dias'),
    (180, 60, 'Plano de 180 dias com troca a cada 60 dias'),
    (360, 60, 'Plano de 360 dias com troca a cada 60 dias');

INSERT INTO
    DIETAS_TREINOS (descricao)
VALUES ('Sem treino'),
    ('Perda de peso'),
    ('Ganho de massa muscular');

-- INSERT INTO
--    CLIENTES (
--        nome,
--        telefone,
--        indicador_cliente_ativo,
--        id_plano,
--        id_dieta
--    )
-- VALUES (
--        'gabriel',
--        '11951269909',
--        true,
--        1,
--        2
--    );
-- 
-- INSERT INTO
--    VALORES (
--        valor_liquido,
--        valor_bruto,
--        id_cliente
--    )
--    VALUES (
--        1,
--        3,
--        1
--    );
-- 
-- INSERT INTO
--     DATAS (
--         id_cliente, data_pagamento, inicio_dieta_treino, inicio_plano, ultima_troca_dieta_treino, proxima_troca_dieta_treino, vencimento_plano
--     )
-- VALUES (
--         1, NOW(), NOW(), NOW(), NOW(), NOW(), NOW()
--     );

SELECT *
FROM    `CLIENTES` c
    INNER JOIN `PLANOS` p ON c.id_plano = p.id_plano
    INNER JOIN `DIETAS_TREINOS` dt ON c.id_dieta = dt.id_dieta
    INNER JOIN `DATAS` ds ON c.id_cliente = ds.id_cliente
    INNER JOIN `VALORES` v ON v.id_cliente = c.id_cliente;

SELECT * FROM `CLIENTES` c ORDER BY `id_cliente` DESC
