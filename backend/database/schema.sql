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