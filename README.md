# Biblioteca 📖

Este é um projeto __Django__ para gerenciar uma Biblioteca, com um sistema de cadastro de livros, usuários e empréstimos.

## Pré-requisitos 📄

Certifique-se de ter os seguintes softwares instalados em sua máquina:

- Python 3.12
- Git

## Clonando o Repositório 🌐

```bash
git clone https://github.com/ryanbritodev/django-fiap.git
cd django-fiap
```

## Configurando o Ambiente Virtual 🔨

Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

## Instalando as Dependências 📲

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## Configurando o Banco de Dados 🎲

Atualize o arquivo `biblioteca/settings.py` para configurar o banco de dados. Por padrão, o projeto está configurado para usar SQLite.

## Executando Migrações 🔄️

Aplique as migrações do banco de dados:

```bash
python manage.py migrate
```

## Executando o Servidor de Desenvolvimento 🧑🏻‍💻

Inicie o servidor de desenvolvimento do __Django__:

```bash
python manage.py runserver
```

Acesse o projeto no navegador através do endereço `http://127.0.0.1:8000`.
