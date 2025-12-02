FastAPI CRUD – Sistema de Clientes

Este projeto é uma API simples de gerenciamento de clientes construída com FastAPI.
O objetivo é demonstrar a lógica básica de um CRUD completo (Create, Read, Update, Delete) usando Python e Pydantic, simulando um banco de dados em memória.

🚀 Tecnologias utilizadas

Python 3.10+

FastAPI

Uvicorn

Pydantic

📌 Funcionalidades

➕ Criar cliente

📄 Listar todos os clientes

🔎 Buscar cliente por ID

✏ Atualizar dados de um cliente existente

❌ Deletar cliente

📁 Estrutura do projeto
📦 fastapi-crud-clientes
│
├── main.py          # Arquivo principal da API
├── models.py        # Modelos Pydantic (Cliente & ClienteBase)
└── README.md        # Documentação do projeto

▶ Como rodar o projeto
1. Instale as dependências:
pip install fastapi uvicorn

2. Execute o servidor:
uvicorn main:app --reload

3. Acesse a documentação automática:

Swagger UI:

http://127.0.0.1:8000/docs


Redoc:

http://127.0.0.1:8000/redoc

📬 Rotas da API
Método	Rota	Descrição
GET	/clientes	Lista todos os clientes
GET	/cliente/{id}	Retorna 1 cliente específico
POST	/cliente	Cria um novo cliente
PUT	/cliente/{id}	Atualiza um cliente existente
DELETE	/cliente/{id}	Remove um cliente


👤 Autor:
Matheus Wolf
Desenvolvedor Back-End em evolução, focado em criar projetos reais e entregar resultado.
