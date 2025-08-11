# Objetivo do Projeto 

O objetivo principal deste projeto é conseguir construir uma simples aplicação com base nos meus conhecimentos sobre `API`, `Banco de Dados` e `Docker`, a fim de testá-los e, se possível, utilizá-los de outras formas em situações futuras.

Nesta aplicação, utilizei como `API` o `FastAPI`, que é simples de entender, funciona em Python e possui documentação própria e automática, o que facilita na hora de testar o código.

Para `Banco de Dados`, utilizei o `MySQL`, que já é muito popular e fácil de colocar em prática.

Por fim, utilizei o `Docker` para que, em situações futuras, eu consiga desenvolver códigos mais elaborados e executá-los em qualquer computador. Este projeto foi uma oportunidade perfeita para começar.

# Como que ele funciona

Este projeto se baseia em uma ideia semelhante à do Twitter. Ele possui usuários com seus nomes, `username` e `id`. Além disso, é possível postar textos com `títulos` e o `corpo do texto`, bem como um `id` para cada postagem feita.


`Ainda não introduzi uma ideia de login, apenas tem as funções de criar usuários e postagens`

Para fazer ele rodar é precisor clonar esse repositório e escrever algumas linhas no terminal para acessar o documento do `Docker`
```bash
docker compose build --no-cache
docker compose up
```
Fazendo isso ele já deve gerar um container do docker de forma que você consigar entrar no link criado e você mesmo criar usuários e postagens.
Para parar o código de funcionar é só dar `Control C`
