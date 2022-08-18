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
