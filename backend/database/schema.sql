CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    url_github TEXT,
    is_public BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS project_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    url TEXT NOT NULL,
    CONSTRAINT fk_projects
    FOREIGN KEY(project_id) 
    REFERENCES projects(id) 
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    is_complete BOOLEAN NOT NULL DEFAULT 0,
    is_public BOOLEAN NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    descricao TEXT,
    editora TEXT,
    paginas_totais INTEGER NOT NULL,
    paginas_lidas INTEGER NOT NULL,
    is_public BOOLEAN NOT NULL DEFAULT 0
);