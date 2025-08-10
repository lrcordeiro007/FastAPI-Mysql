# Objetivo do Projeto 

O objetivo principal desse projeto é conseguir contruir uma simples aplicação dos meus conhecimentos sobre `API`, `Banco de Dados` e `Docker`, afim de testar eles e se possível utilizar de outras formas em situações futuras.

Nessa aplicação eu utilizei como `API` o `FastAPI`, o qual é simples de enteder, funcionar em python e ter uma documentação própria e automática, o que facilita na hora de testar o código.

Para `Banco de Dados` eu utilizei o `MySQL` o qual já muito popular e fácil de colocar em prática.

E por fim utilizei o `Docker` para que em situações futuras eu consiga desenvolver códigos mais elaborados e consiga colocar ele para rodar em qualquer computador e esse projeto foi uma oportunidade perfeita para poder começar.

# Como que ele funciona

Esse projeto de basea em uma ideia semelhante a um Twiter, ele possui os seus usuários com seus nomes , `username` e seus `id`, além disso é possivel postar textos com `títulos` e o `corpo do texto`, como também um `id` para cada postagem feita.


`Ainda não introduzi uma ideia de login, apenas tem as funções de criar usuários e postagens`

Para fazer ele rodar é precisor clonar esse repositório e escrever algumas linhas no terminal para acessar o documento do `Docker`
```bash
docker compose build --no-cache
docker compose up
```
Fazendo isso ele já deve gerar um container do docker de forma que você consigar entrar no link criado e você mesmo criar usuários e postagens.
