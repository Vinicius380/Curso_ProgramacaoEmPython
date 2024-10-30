CREATE DATABASE cadastro; 

USE cadastro;

CREATE TABLE contato (
    nome VARCHAR(150),
    endereco VARCHAR(60),
    telefone VARCHAR(16),
    email VARCHAR(100)
);

INSERT INTO contato(nome,endereco,telefone,email)
values("a","b","123456789","","c@f");