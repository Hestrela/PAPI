from database.connection import get_connection
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/")
def list_projects():
    with get_connection() as conexao:
        resultado = conexao.execute("SELECT id, titulo, descricao, url_github, is_public FROM projects")
        linhas = resultado.fetchall()
        return [dict(linha) for linha in linhas]

class ProjectCreate(BaseModel):
    titulo: str
    descricao: str | None = None
    url_github: str | None = None
    is_public: bool = True

@router.post("/")
def create_project(project: ProjectCreate):
    with get_connection() as conexao:
        resultado = conexao.execute("INSERT INTO projects (titulo, descricao, url_github, is_public) VALUES(?, ?, ?, ?)", (project.titulo, project.descricao, project.url_github, project.is_public))
        novo_id = resultado.lastrowid
        return {"id": novo_id, **project.model_dump()}

class LinkCreate(BaseModel):
    titulo: str 
    url: str

@router.post("/{project_id}/links")
def add_project_link(project_id: int, link: LinkCreate):
    with get_connection() as conexao:
        resultado = conexao.execute("INSERT INTO project_links (titulo, url, project_id) VALUES(?, ?, ?)", (link.titulo, link.url, project_id))
        novo_id = resultado.lastrowid
        return {"id": novo_id, **link.model_dump()}