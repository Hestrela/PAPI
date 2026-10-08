from fastapi import APIRouter
from database.connection import get_connection
from pydantic import BaseModel

router = APIRouter(prefix="/games", tags=["Games"])

@router.get("/")
def list_games():
    with get_connection as conexao:
        resultado = conexao.execute("SELECT id, titulo, descricao, is_complete, is_public FROM games")
        linhas = resultado.fetchall()
        return [dict(linha) for linha in linhas]

class GameCreate(BaseModel):
    titulo : str
    descricao : str | None = None
    is_complete : bool = False
    is_public : bool = False

@router.post("/")
def create_game(game : GameCreate):
    with get_connection as conexao:
        resultado = conexao.execute("INSERT (titulo, descricao, is_complete, is_public) VALUE (?, ?, ?, ?)", (game.titulo, game.descricao, game.is_complete, game.is_public))
        novo_id = resultado.lastrowid
        return {"id" : novo_id, **game.model_dump()}