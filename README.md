# Backend de uma API de Blog de Artigos

Uma API REST de um blog de artigos construída usando o Django e Django Rest Framework para o teste técnico da Samplemed.

## Instalação

### Requerimentos

- Python
- Django

Mais os itens do requirements.txt

## QuickStart

- Clone o repositório através do comando:
```
    git clone https://github.com/Gustavo274/blog_api.git
```
- Já com o repositório clonado, acesse ele e crie um ambiente virtual e em seguida ative-o, através dos comandos:
```
    python -m venv env 
    source env/bin/activate
```
- Instale os requerimentos do requirements.txt através do comando:
```
    pip install -r requirements.txt
```
- Faça as migrations através dos comandos:
```
    ./manage.py makemigrations && ./manage.py migrate
```
- Crie um superusuário através do comando:
```
    ./manage.py createsuperuser
```
- Inicie o servidor: 
```
    ./manage.py runserver
```

**OBS: Após iniciar o servidor, você pode testá-lo tanto pelo Postman, como pela URL: http://127.0.0.1:8000/, onde neste URL haverá uma overview das URLs da API.**

## Diagrama das Tabelas da aplicação

![Imagem](https://github.com/Gustavo274/blog_api/blob/main/DBML_do_blog.png)

## Tabela de Endpoints com funcionalidades da API

| **Função**                          | **REQUEST** | **Endpoint**                                             | **Autorização** | **data do formulário**             |
|-------------------------------------|-------------|----------------------------------------------------------|-----------------|------------------------------------|
| Criar um novo usuário               |     POST    | http://127.0.0.1:8000/user/register/                     |     Nenhuma     |     username, email e password     |
| Listar todos os usuários.           |     GET     | http://127.0.0.1:8000/user/                              |    Basic Auth   |                                    |
| Detalhar usuário.                   |     GET     | http://127.0.0.1:8000/user/{int:id}/                     |    Basic Auth   |                                    |
| Atualizar detalhes de um usuário    |  PUT, PATCH | http://127.0.0.1:8000/user/{int:id}/                     |    Basic Auth   |                                    |
| Deletar um usuário                  |    DELETE   | http://127.0.0.1:8000/user/{int:id}/                     |    Basic Auth   |                                    |
| Criar um novo artigo.               |     POST    | http://127.0.0.1:8000/articles/create/                   |    Basic Auth   | title, subtitle, content e keyword |
| Listar os artigos já criado.        |     GET     | http://127.0.0.1:8000/articles/                          |     Nenhuma     |                                    |
| Detalhar um artigo.                 |     GET     | http://127.0.0.1:8000/articles/{int:pk}/                 |    Basic Auth   |                                    |
| Atualizar detalhes de um artigo.    |  PUT, PATCH | http://127.0.0.1:8000/articles/{int:pk}/                 |    Basic Auth   | title, subtitle, content e keyword |
| Deletar um artigo.                  |    DELETE   | http://127.0.0.1:8000/articles/{int:pk}/                 |    Basic Auth   |                                    |
| Criar um novo comentário.           |     POST    | http://127.0.0.1:8000/articles/{int:pk}/comment/create/  |    Basic Auth   |               content              |
| Listar os comentários de um artigo. |     GET     | http://127.0.0.1:8000/articles/{int:pk}/comment/         |     Nenhuma     |                                    |
| Detalhar um comentário.             |     GET     | http://127.0.0.1:8000/articles/{int:pk}/comment/{int:id} |     Nenhuma     |                                    |
| Atualizar um comentário existente.  |  PUT, PATCH | http://127.0.0.1:8000/articles/{int:pk}/comment/{int:id} |    Basic Auth   |               content              |
| Deletar um comentário existente.    |    DELETE   | http://127.0.0.1:8000/articles/{int:pk}/comment/{int:id} |    Basic Auth   |                                    |
| Gerar um token de autenticação JWT. |     POST    | http://127.0.0.1:8000/token/                             |     Nenhuma     |         username e password        |
