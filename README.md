# 📒 Agenda de Contatos Online

Um sistema web simples para gerenciar contatos pessoais, desenvolvido com **Flask**, **PostgreSQL** e **Docker**. Ele implementa um sistema de **autenticação de usuários** e permite **CRUD completo** (criar, visualizar, editar e excluir contatos) de maneira individualizada para cada usuário.

---

## 🧩 Estrutura do Projeto

```
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── extensions.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   └── style.css
│   └── templates
│       ├── add_contact.html
│       ├── base.html
│       ├── dashboard.html
│       ├── edit_contact.html
│       ├── index.html
│       ├── login.html
│       └── register.html
├── docker-compose.yml
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── e5d01cfe1a7b_add_user_id_to_contact.py
├── requirements.txt
└── run.py
```

---

## 🚀 Tecnologias Utilizadas

- **Python 3.8+**
- **Flask** – microframework para aplicações web
- **Flask-Login** – controle de autenticação
- **PostgreSQL** – banco de dados relacional
- **SQLAlchemy** – ORM para mapeamento objeto-relacional
- **Jinja2** – sistema de templates para HTML dinâmico
- **Docker & Docker Compose** – containerização da aplicação e do banco
- **Alembic** – controle de versionamento do banco (migrations)
- **HTML5 & CSS3** – construção da interface web


---

## ⚙️ Como Rodar

### 🔧 Sem Docker (modo manual)

1. Clone o repositório:
   ```bash
   git clone https://github.com/gcarucce10/flask-contacts.git
   cd flask-contacts

2. Instale os requisitos:
   ```bash
   pip install -r requirements.txt

3. Rode o app:
   ```bash
   python run.py

4. 🐳 Também é possível rodar o projeto com Docker (Recomendado):
    ```bash
   docker-compose up --build
    
5. Acesse no navegador:
   [http://localhost:5000](http://localhost:5000)

## ✅ Funcionalidades

- 🔐 Autenticação de usuários (registro, login, logout)
- ✅ Adicionar contato
- ✅ Editar contato
- ✅ Remover contato
- ✅ Listar contatos (somente os do usuário logado)


## 📌 Próximos Passos

- 🔑 Implementar hash de senha com segurança (ex: bcrypt)
- 🔍 Adicionar busca de contatos por nome, email ou telefone
- 📦 Criar uma API RESTful (usando Flask-RESTful ou Flask-RESTX)
- 🖼️ Permitir upload de imagem de perfil para os contatos
- 🌐 Fazer deploy da aplicação (Render, Railway, ou AWS)
- 🧪 Adicionar testes automatizados com pytest e cobertura de testes
- 🎨 Melhorar o layout com um design responsivo e moderno (ex: Bootstrap ou Tailwind)
- 📊 Adicionar paginação e ordenação na lista de contatos
- 🔔 Adicionar sistema de notificações ou alertas para ações realizadas




