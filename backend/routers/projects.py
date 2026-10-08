from fastapi import HTTPException
from database.connection import get_connection
from fastapi import APIRouter
from pydantic import BaseModel

class ProjectCreate(BaseModel):
    titulo: str
    descricao: str | None = None
    url_github: str | None = None
    is_public: bool = True

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/")
def list_projects():
    with get_connection() as conexao:
        resultado = conexao.execute("SELECT p.id AS project_id, p.titulo AS project_titulo, p.descricao, p.url_github, p.is_public, l.id AS link_id, l.titulo AS link_titulo, l.url AS link_url FROM projects p LEFT JOIN project_links l ON p.id = l.project_id;")
        linhas = resultado.fetchall()
        projetos_map = {}
        for linha in linhas:
            p_id = linha["project_id"]
            if p_id not in projetos_map:
                projetos_map[p_id] = {
                    "id" : p_id,
                    "titulo" : linha["project_titulo"],
                    "descricao" : linha["descricao"],
                    "url_github" : linha["url_github"],
                    "is_public" : bool(linha["is_public"]),
                    "links" : []
                }
            if linha["link_id"] is not None:
                projetos_map[p_id]["links"].append({
                    "id": linha["link_id"],
                    "titulo": linha["link_titulo"],
                    "url": linha["link_url"]
                })

        return list(projetos_map.values())

@router.post("/")
def create_project(project: ProjectCreate):
    with get_connection() as conexao:
        resultado = conexao.execute("INSERT INTO projects (titulo, descricao, url_github, is_public) VALUES(?, ?, ?, ?)", (project.titulo, project.descricao, project.url_github, project.is_public))
        novo_id = resultado.lastrowid
        return {"id": novo_id, **project.model_dump()}

@router.put("/{project_id}")
def edit_project(project: ProjectCreate, project_id: int):
    with get_connection() as conexao:
        resultado = conexao.execute("UPDATE projects SET titulo = ?, descricao = ?, url_github = ?, is_public = ? WHERE id = ?", (project.titulo, project.descricao, project.url_github, project.is_public, project_id))
        linhas_afetadas = resultado.rowcount
        if linhas_afetadas == 0:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")
        else:
            return {"id": project_id, **project.model_dump()}

@router.delete("/{project_id}")
def delete_project(project_id: int):
    with get_connection() as conexao:
        resultado = conexao.execute("DELETE FROM projects WHERE id = ?", (project_id,))
        linhas_deletadas = resultado.rowcount
        if linhas_deletadas == 0:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")
        else:
            return {"message": "Projeto deletado com sucesso!"}

class LinkCreate(BaseModel):
    titulo: str 
    url: str

@router.post("/{project_id}/links")
def add_project_link(project_id: int, link: LinkCreate):
    with get_connection() as conexao:
        resultado = conexao.execute("INSERT INTO project_links (titulo, url, project_id) VALUES(?, ?, ?)", (link.titulo, link.url, project_id))
        novo_id = resultado.lastrowid
        return {"id": novo_id, **link.model_dump()}




