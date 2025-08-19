
# FastAPI-MySQL
# 💡 Sobre o Projeto
Este projeto é uma `API RESTful` robusta e moderna, desenvolvida para demonstrar a integração poderosa e eficiente entre o FastAPI e o banco de dados `MySQL`. A aplicação foi arquitetada como uma base sólida para o desenvolvimento de microsserviços e aplicações web que requerem alta performance e um sistema de gerenciamento de banco de dados relacional confiável.

O foco principal do projeto é a simplicidade e a manutenibilidade. Ele implementa as operações essenciais de um `CRUD` (Create, Read, Update, Delete) em um modelo de dados simples, permitindo a gestão de recursos de forma intuitiva e segura. A ideia é semelhante à de uma rede social, onde você pode criar usuários e postagens.

# ✨ Recursos
API RESTful Completa: Operações CRUD para gestão de dados.

- Performance Excepcional: Aproveita as vantagens de assincronicidade do FastAPI, resultando em respostas rápidas e baixo consumo de recursos.

- Integração com MySQL: Utiliza o `sqlalchemy` para uma comunicação ORM (Object-Relational Mapping) com o banco de dados, simplificando a manipulação de dados.

- Padrão de Código: Código limpo, modular e seguindo as melhores práticas de desenvolvimento Python.

- Documentação Automática: O FastAPI gera automaticamente a documentação interativa da API (Swagger UI e ReDoc), facilitando o teste e a compreensão dos endpoints.

- Dockerização: Contêineres Docker e Docker Compose para isolamento e portabilidade, garantindo um ambiente de desenvolvimento e produção consistente.

- Front-end Simples: Uma demonstração de como a API pode ser consumida por um front-end, utilizando templates HTML.

# 🛠️ Tecnologias Utilizadas
Python 3.10+

-  FastAPI

-  MySQL

-  SQLAlchemy

-  Pydantic

-  Docker & Docker Compose

-  Jinja2

# 🚀 Como Iniciar
Pré-requisitos
Certifique-se de ter o Docker e o Docker Compose instalados em seu sistema.

# ⚙️ Instalação e Execução
A maneira mais recomendada para executar este projeto é utilizando Docker Compose, pois ele gerencia tanto a aplicação FastAPI quanto o contêiner do banco de dados MySQL, garantindo que todas as dependências estejam no lugar correto.

Clone o repositório:

```Bash

git clone https://github.com/lrcordeiro007/FastAPI-Mysql.git
cd FastAPI-Mysql
```
Construa e inicie os contêineres:

```Bash

docker-compose up --build --no-cache
```
Isso fará o download da imagem do MySQL, construirá a imagem da aplicação FastAPI e iniciará ambos os serviços. O contêiner do FastAPI estará acessível na porta 8000.

Acesso à Aplicação
Após a execução do Docker Compose, a aplicação estará disponível nos seguintes endereços:

API Principal: `http://localhost:8000/`

Documentação Interativa (Swagger UI): `http://localhost:8000/docs`

Documentação (ReDoc): `http://localhost:8000/redoc`

O template HTML de demonstração, que consome os dados da API, também estará acessível em `http://localhost:8000/`.

Para interromper a execução, basta pressionar Ctrl + C no terminal.

# 📂 Estrutura do Projeto

- src/: Contém o código-fonte da aplicação.

- - main.py: Onde a aplicação FastAPI é inicializada e os endpoints são definidos.

- - models.py: Define os modelos de dados ORM.

- - database.py: Configuração da conexão com o banco de dados.

- - routes/: Módulo de rotas para organizar os endpoints.

- docker-compose.yml: Arquivo para orquestração de serviços com Docker Compose.

- Dockerfile: Define a imagem Docker da aplicação.

- requirements.txt: Dependências do projeto.

- templates/: Diretório para os templates HTML.
