Elaborar um arquivo README contendo nome e RM do aluno (ou da dupla), descrevendo detalhes do projeto, instruções
de uso, requisitos, dependências e demais informações relevantes ao projeto. Será avaliada a clareza e organização do
conteúdo apresentado. Entregável: Arquivo README.

# # Cadastro e login usando CPF em python

## Participantes:
* <h4> Gustavo bezerra Assumção </h4> RM: 553076
* <h4> Jeferson Gabriel </h4> RM: 

## Instrucoes de uso:

1. Para poder utilizar o codigo corretamente se deve selecionar o caminho que queira seguir.
2. Deve digitar " 1 " caso ja tenha cadastro, e ira automanticamnete pedir o cpf para poder efetuar o login usando o cpf informado. <br> Alem disso, o numero " 2 " é utilizado para cadastro do paciente, onde o usuario precisara informar o nome, idade, cpf e numero de telefone. <br> Logo, para as demais respostas o codigo ira mostar uma mensagem de erro. 

## Detalhes de como o projeto foi construido:

* Primeiramente foi utilizado uma biblioteca chamada "pandas" para criar uma tabela onde os dados sera armazenados e exibidos.

* No momento seguinte, foi criando dois dicionarios que daram origem as tabelas dos paceintes cadastrados e dos pacintes que ainda nao possuem cadastro. <br> Alem disso, é nesses diciorarios que os dados dos pacientes serao armazenados.

* foi chamado a biblioteca do pandas para poder criar as funcoes e permitir a transformacao do dicionario em tabela

* foi criada 2 funcoes uma para cadastro e outra para verificacao dos pacientes

* na funcao de cadastro:

    1. foi utilizando uma estrutura de repeticao "while True", que formara um loop de repeticao infinito ate o usuario quiser parar.

    2. é solicitado 4 informacoes do usuario, sendo: seu nome, idade, cpf e telefone. <br> Alem disso, ira continuar perguntando enquanto o usuario nao encerrar o codigo

    3. primeira estrutura de condicao: se o valor do cpf nao estiver no banco de dados, ira rodar o codigo adicionado todos os dados informados pelo usuario na biblioteca de cadastro. <br> No entanto, se ja esxistir o cpf informado, ira informar o usuario que ele ja possui cadastro.

    4. cria uma variavel que pergunta ao usuario se ele deseja parar. <br> Alem disso, o 'upper()' transforma automanticamente tudo o que o usuario colocar em letra maiuscula

    5. segunda estrutura de condicao: se o valor digitado pelo usuario for o " PARAR " o codigo ira parar. Caso contrario, o codigo ira seguir em frente
    
    6. finalizacao da funcao cadastro, retornado e transformando os valores do dicionario de cadastro em uma tabela

* na funcao de login:

    1. pergunta o cpf, a resposta deve ser em numero
    
    2. estrutura de condicao: se existir o numero do cpf no dicionario cadastro, ira rodar o codigo

    3. cria uma variavel que recebe a posicao exata do numero de cpf que deu igual ao numero que o usuario colocou

    4. adiciona os mesmos dados do dicionario cadastro no outro dicionario chamado cadastrado.

    5. se nao encontrar o cpf dentro do dicionario cadastro ira printar uma mensagem de erro

    6. finalizacao da funcao login, retornado e transformando os valores do dicionario cadastrado em uma tabela

* criando uma variavel que pergunta se o usuario que fazer o login ou se cadastrar. <br> Obs: a escolha sera feita por numeros. 1 - para login e 2- para cadastro

* estutura de condicao: se o valor for 1, ira iniciar a funcao login e mostar os resultados no final. <br> Se for 2, ira iniciar a funcao de cadastro. <br> Se nao for nenhuma das duas ira dar erro



