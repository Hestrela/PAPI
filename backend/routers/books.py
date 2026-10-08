from database.connection import get_connection
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/")
def list_books():
    with get_connection as conexao:
        resultado = conexao.execute("SELECT id, titulo, descricao, editora, paginas_totais, paginas_lidas, is_public FROM books")
        linhas = resultado.fetchall()
        return [dict(linha) for linha in linhas]

class BookCreate(BaseModel):
    titulo : str
    autor : str
    descricao : str | None = None
    editora : str | None = None
    paginas_totais : int
    paginas_lidas : int
    is_public : bool = False


@router.post("/")
def create_book(book : BookCreate):
    with get_connection as conexao:
        resultado = conexao.execute("INSERT (titulo, autor, descricao, editora, paginas_totais, paginas_lidas, is_public) VALUES(?, ?, ?, ?, ?, ?, ?)", (book.titulo, book.autor, book.descricao, book.editora, book.paginas_totais, book.paginas_lidas, book.is_public))
        novo_id = resultado.lastrowid
        return {"id" : novo_id, **book.model_dump()}