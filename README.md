# Validação de Números de Telefone com Django

Este projeto foi desenvolvido usando **Django** e **Django Rest Framework**, com o objetivo de criar um sistema que consome uma API para verificar números de telefone e retornar informações detalhadas. O sistema também inclui uma área de registro e login, com medidas de segurança para garantir que os usuários registrem senhas fortes.

## Funcionalidades

- **Registro e Login de Usuários:**
  - O sistema exige que os usuários se registrem e façam login antes de acessar a funcionalidade de validação de números de telefone.
  - Durante o registro, o sistema impõe a criação de senhas fortes, impedindo que o usuário registre senhas consideradas fracas.

- **Validação de Números de Telefone:**
  - Após o login, o usuário pode inserir um número de telefone para validação.
  - O número é consultado em uma API externa para verificar sua validade e retornar informações relacionadas, como localização e operadora.
  - Se o número for válido, as informações são exibidas em uma página de resultados e registradas no banco de dados.
  - Se o número for inválido, uma mensagem de erro será exibida.

## Tecnologias Utilizadas

- **Django:** Framework principal usado para desenvolver o backend do projeto.
- **Django Rest Framework:** Utilizado para criar as APIs que consomem a API externa de validação de números de telefone.
- **HTML/CSS:** Usado para criar e estilizar as páginas de login, registro e resultados.
- **SQLite:** Banco de dados utilizado para armazenar informações de usuários e registros de validações de números de telefone.

## Estrutura do Projeto

├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   ├── informar_telefone.html
│   │   ├── dados_telefone.html
│   └── ...
└── ...


## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo

2 **Crie um ambiente virtual e ative-o:**
   ```bash 
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate  # Windows

3 **Instale as dependências:**
    ```bash 
    pip install -r requirements.txt

4 **Realize as migrações do banco de dados:**
    ```bash
    python manage.py migrate

5 **Inicie o servidor:**
    ```bash
    python manage.py runserver

## Acesse o projeto:

Abra o navegador e acesse [http://localhost:8000](http://localhost:8000).

## Uso

### Registro:

- Acesse a página de registro para criar uma conta. O sistema não permite senhas fracas.
- Insira um nome de usuário, senha e confirme a senha.
- Após o registro, faça login no sistema.

### Login:

- Acesse a página de login.
- Insira suas credenciais para acessar a funcionalidade de validação de números de telefone.

### Validação de Números de Telefone:

- Após o login, você será redirecionado para a página onde poderá inserir um número de telefone.
- Submeta o número para verificar sua validade.
- Se o número for válido, as informações serão exibidas na página de resultados.
- Se o número for inválido, uma mensagem de erro será exibida.
