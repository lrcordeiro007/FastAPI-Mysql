# FastAPI-Mysql
Ínico de um projeto que utiliza de uma API (FastAPI) em conjunto com um banco de dados (MySQL)


Ínico no aprendizado na contrução de sites por conta própria, nesse instante busco apenas utilizar o 
FastAPI como forma de fazer uma ligação direta com o meu banco de dados que eu mesmo criei.no

Nesse instante, como o FastAPI nos fornece um auxilio muito bom na hora de desenvolver uma API eu escolhi ele
pelo motivo de eu conseguir utilizar do seu /docs para "escapar" de ter que fazer uma interface para o site.
Além de uma mais fácil na hora de usar o terminal para lançar ele na rede.

Futuramente procuro melhorar esse projeto, fazendo uma interface melhor para adicionar users e posts no meu banco de dados,
assim como adicionar mais tabelas como ligações entre elas. 

# Como ele funciona ?

Basicamente ele se baseia em um banco de dados simples com duas tabelas ou "tables", quais são os "users" os usuários do site 
que possuem o nome e o id como colunas de identificação, e também os "posts" que são frases que podem ser postadas até um certo número 
de caracteres, possuindo título, id e content como colunas.

Sabendo disso, implentamos o uso da FastAPI e seu auxílio no /docs para que possamos acrescentar "users" e "posts" e depois com o acessando o 
banco de dados, eu utilizo o próprio MySQL Workbench para visualizar se esta funcionando ou não. Após acessar o banco de dados é possível verificar 
oque foi adicionado utilizando de comando SQL ao nosso favor.

Para fazer funcionar você precisa criar um espaço virtual, além de ter que baixar os pacotes com sql_alchemy e fastapi para que o código funcione 
de maneira desejada, além de ter que usar do uvicorn para que o fastapi funcione.

outro ponto importante é que no código é preciso de um nome e uma senha do banco de dados, de preferencia crie ou coloque o seu mesmo.
