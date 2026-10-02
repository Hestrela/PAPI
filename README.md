# 🚀 PAPI - Personal API

Uma API pessoal flexível e centralizada desenvolvida para armazenar, gerenciar e servir dados sobre minha vida, projetos, rotina acadêmica e entretenimento.

O coração desse projeto é funcionar como a **fonte única da verdade (Single Source of Truth)** para automatizar a presença digital: alimentando portfólios web, integrando rotinas de automação com IA e servindo listas de tarefas do dia a dia.

---

## 💡 A Ideia & Visão do Projeto

- **Portfólio Dinâmico:** Um dia, com o portfólio hospedado em plataformas como Vercel, o frontend consultará o **PAPI** para exibir projetos, repositórios do GitHub, links extras e destaques profissionais sempre atualizados sem precisar de novos deploys.
- **Automações com IA & n8n:** Conexão direta com pipelines de automação (como n8n) integrados a modelos de IA locais para cadastrar projetos automaticamente a partir de commits/novos repositórios, enriquecer descrições e atualizar metadados de forma autônoma.
- **Hub Pessoal de Produtividade & Lazer:** Centralização de atividades e datas de provas da faculdade para abastecer dashboards/to-do lists, além de acompanhar livros lidos, jogos zerados e outros hobbies.
- **Hospedagem "Home Server" (Galaxy J7 Prime 📱):** Rodando 24/7 direto em um smartphone antigo reaproveitado como servidor local — hardware sustentável, consumo mínimo de energia e disponibilidade praticamente ininterrupta!

---

## 🛠️ Tecnologias

- **Linguagem:** Python 3
- **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/) (rápido, tipado e com documentação automática Swagger/OpenAPI)
- **Servidor ASGI:** Uvicorn
- **Banco de Dados:** SQLite (leve, confiável e sem overhead de banco externo)
- **Ambiente de Execução:** Linux / Termux no Samsung Galaxy J7 Prime

---

## 📌 Funcionalidades e Roadmap

- [x] **Projetos Pessoais & Links:** CRUD completo de projetos, visibilidade pública/privada, URLs do GitHub e links complementares.
- [ ] **Integração com n8n & IA:** Endpoints protegidos para ingestão automatizada de novos projetos.
- [ ] **Módulo Acadêmico:** Registro de atividades, prazos de entrega e datas de provas para integração com lista de tarefas.
- [ ] **Módulo de Entretenimento:**
  - 📚 Livros lidos, notas e status de leitura.
  - 🎮 Jogos zerados e backlog.
- [ ] **Integração com Frontend:** Consumo dos dados pelo portfólio estático/dinâmico.

---

## 📂 Estrutura do Projeto

```plaintext
PAPI/
├── backend/
│   ├── database/
│   │   ├── connection.py    # Gerenciamento de conexões SQLite
│   │   └── schema.sql       # Definição das tabelas
│   ├── routers/
│   │   └── projects.py      # Endpoints para gerenciamento de projetos
│   ├── config.py            # Variáveis de ambiente e configurações
│   └── main.py              # Ponto de entrada FastAPI
├── requirements.txt         # Dependências do projeto
├── .env.example             # Exemplo de configuração de variáveis
└── README.md                # Documentação do projeto
```

---

## 🚀 Como Executar Localmente

### 1. Pré-requisitos
- Python 3.10+ instalado
- `pip` e `venv` (uv recomendado)

### 2. Clonar e Configurar Ambiente
```bash
# Clone o repositório
git clone https://github.com/Hestrela/PAPI.git
cd PAPI

# Crie e ative um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate  # No Linux/Termux/macOS
# .venv\Scripts\activate   # No Windows

# Instale as dependências
pip install -r requirements.txt

# Caso já tenha uv
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```


### 3. Configurar Variáveis de Ambiente
Copie o arquivo `.env.example` para `.env` e configure conforme necessário:
```bash
cp .env.example .env
```

### 4. Rodar o Servidor
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

#### Caso estiver rodando em um dispositivo mais recente com fastapi em versões >=0.111.0:
```bash
uv run fastapi dev backend/main.py
```

Acesse a documentação interativa da API no navegador:
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📱 Hardware & Servidor

| Item | Especificação |
| :--- | :--- |
| **Dispositivo** | Samsung Galaxy J7 Prime |
| **Finalidade** | Servidor 24/7 de baixo custo e baixo consumo |
| **Ambiente** | Termux / Linux Environment |
| **Acesso** | Rede local com túnel/proxy reverso para consumo externo |

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [LICENSE](https://github.com/Hestrela/PAPI/blob/main/LICENSE) para mais informações.
