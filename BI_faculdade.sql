DROP DATABASE IF EXISTS BI_faculdade;

CREATE DATABASE BI_Faculdade;

USE BI_Faculdade;

CREATE TABLE dim_estudante (
    tf_estudante bigint,
    nome_estudante VARCHAR(255),
    matricula VARCHAR(255)
);

CREATE TABLE dim_disciplina (
    tf_disciplina bigint,
    nome_disciplina VARCHAR(255) NOT NULL
);

CREATE TABLE fato_notas (
    tf_estudante bigint,
    tf_disciplina bigint,
    nota double
);

SELECT 'fato_notas' AS Tabela;
SELECT * FROM fato_notas;