import sqlite3
from config import DATABASE_PATH
from pathlib import Path

SCHEMA_PATH = Path(__file__).parent / "schema.sql"

def get_connection():
    conexao = sqlite3.connect(DATABASE_PATH)
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao

def init_db():
    conteudo_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    
    with get_connection() as conexao:
        conexao.executescript(conteudo_sql)
    conexao.close()