-- Criação do banco de dados faculdade
DROP DATABASE IF EXISTS faculdade;
CREATE DATABASE faculdade;
USE faculdade;

-- Criação da tabela de estudantes
CREATE TABLE estudantes (
    rgm INT PRIMARY KEY,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Populando a tabela de estudantes com 5 registros
INSERT INTO estudantes (rgm, cpf, nome, email) VALUES
(123456, '111.222.333-44', 'Ana Silva', 'ana.silva@email.com'),
(234567, '222.333.444-55', 'Bruno Oliveira', 'bruno.oliveira@email.com'),
(345678, '333.444.555-66', 'Carlos Pereira', 'carlos.pereira@email.com'),
(456789, '444.555.666-77', 'Daniela Santos', 'daniela.santos@email.com'),
(567890, '555.666.777-88', 'Eduardo Costa', 'eduardo.costa@email.com');

-- Criação da tabela de disciplinas
CREATE TABLE disciplinas (
    codigo INT PRIMARY KEY,
    nome_disciplina VARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL
);

-- Populando a tabela de disciplinas com 3 disciplinas de computação
INSERT INTO disciplinas (codigo, nome_disciplina, carga_horaria) VALUES
(1001, 'Banco de Dados', 80),
(1002, 'Programação Orientada a Objetos', 60),
(1003, 'Estrutura de Dados', 60);

-- Criação da tabela de matrículas
CREATE TABLE matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rgm_estudante INT,
    codigo_disciplina INT,
    semestre VARCHAR(10) NOT NULL,
    FOREIGN KEY (rgm_estudante) REFERENCES estudantes(rgm),
    FOREIGN KEY (codigo_disciplina) REFERENCES disciplinas(codigo),
    UNIQUE KEY (rgm_estudante, codigo_disciplina, semestre)
);

-- Populando a tabela de matrículas para todos os estudantes em todas as disciplinas (semestre 2023/1)
INSERT INTO matriculas (rgm_estudante, codigo_disciplina, semestre) VALUES
-- Ana Silva em todas as disciplinas
(123456, 1001, '2023/1'),
(123456, 1002, '2023/1'),
(123456, 1003, '2023/1'),
-- Bruno Oliveira em todas as disciplinas
(234567, 1001, '2023/1'),
(234567, 1002, '2023/1'),
(234567, 1003, '2023/1'),
-- Carlos Pereira em todas as disciplinas
(345678, 1001, '2023/1'),
(345678, 1002, '2023/1'),
(345678, 1003, '2023/1'),
-- Daniela Santos em todas as disciplinas
(456789, 1001, '2023/1'),
(456789, 1002, '2023/1'),
(456789, 1003, '2023/1'),
-- Eduardo Costa em todas as disciplinas
(567890, 1001, '2023/1'),
(567890, 1002, '2023/1'),
(567890, 1003, '2023/1');

-- Criação da tabela de notas bimestrais
CREATE TABLE notas_bimestrais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_matricula INT,
    bimestre INT CHECK (bimestre BETWEEN 1 AND 4),
    nota DECIMAL(4,2) CHECK (nota BETWEEN 0 AND 10),
    FOREIGN KEY (id_matricula) REFERENCES matriculas(id)
);

-- Populando a tabela de notas com valores aleatórios (incluindo alguns abaixo de 6)
-- Usando a função RAND() do MySQL para gerar valores aleatórios

-- Notas para Ana Silva
INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 1, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 123456;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 2, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 123456;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 3, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 123456;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 4, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 123456;

-- Notas para Bruno Oliveira (garantindo pelo menos uma nota abaixo de 6)
INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 1, ROUND(RAND() * 5, 2) FROM matriculas WHERE rgm_estudante = 234567;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 2, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 234567;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 3, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 234567;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 4, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 234567;

-- Notas para Carlos Pereira
INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 1, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 345678;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 2, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 345678;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 3, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 345678;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 4, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 345678;

-- Notas para Daniela Santos (garantindo pelo menos uma nota abaixo de 6)
INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 1, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 456789;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 2, ROUND(RAND() * 5, 2) FROM matriculas WHERE rgm_estudante = 456789;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 3, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 456789;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 4, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 456789;

-- Notas para Eduardo Costa
INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 1, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 567890;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 2, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 567890;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 3, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 567890;

INSERT INTO notas_bimestrais (id_matricula, bimestre, nota)
SELECT id, 4, ROUND(RAND() * 10, 2) FROM matriculas WHERE rgm_estudante = 567890;

-- Visualização dos dados inseridos (opcional - para verificação)
SELECT 'Estudantes' AS Tabela;
SELECT * FROM estudantes;

SELECT 'Disciplinas' AS Tabela;
SELECT * FROM disciplinas;

SELECT 'Matrículas' AS Tabela;
SELECT * FROM matriculas;

SELECT 'Notas Bimestrais' AS Tabela;
SELECT * FROM notas_bimestrais;