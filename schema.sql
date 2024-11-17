DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa TEXT NOT NULL,
    contato TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    cidade TEXT NOT NULL,
    segmento TEXT NOT NULL
);

DROP TABLE IF EXISTS projetos;

CREATE TABLE projetos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT NOT NULL,
    servicos TEXT NOT NULL,
    valor TEXT NOT NULL,
    inicio TEXT NOT NULL,
    fim TEXT NOT NULL
);

DROP TABLE IF EXISTS servicos;

CREATE TABLE servicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor TEXT NOT NULL,
    segmento TEXT NOT NULL
);