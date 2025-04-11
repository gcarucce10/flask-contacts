# 📒 Agenda de Contatos Online

Um pequeno sistema CRUD (Create, Read, Update, Delete) desenvolvido com **Flask**, **PostgreSQL**, **HTML** e **CSS** para gerenciamento de contatos. O projeto utiliza **Docker** para facilitar o ambiente de desenvolvimento e pode ser facilmente estendido com novos recursos.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.8+**
- **Flask** – microframework para aplicações web
- **PostgreSQL** – banco de dados relacional
- **SQLAlchemy** – ORM para manipulação do banco
- **Jinja2** – sistema de templates HTML
- **HTML5 e CSS3** – para a interface do usuário
- **Docker & Docker Compose** – para containerização da aplicação e do banco

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

4. Acesse no navegador:
   [http://localhost:5000](http://localhost:5000)

5. Também é possível rodar o projeto com Docker (Recomendado):
    ```bash
   docker-compose up --build

## Funcionalidades

- ✅ Adicionar contato
- ✅ Editar contato
- ✅ Remover contato
- ✅ Listar contatos

## 📌 Próximos Passos

- 🔐 Adicionar autenticação de usuário  
- 🔍 Implementar busca por nome, email ou telefone  
- 🌐 Criar uma versão com API REST (Flask RESTful)  
- 💾 Adicionar persistência de imagens de perfil  
- ☁️ Fazer deploy na AWS ou Render  
- 🧪 Testes automatizados (pytest)
- 🎨 Melhorar o design e a usabilidade das páginas com um layout mais moderno 




