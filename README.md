# Suporte psicológico para alunos de exatas
 
Orientação para um semi-diagnóstico do transtorno de ansiedade e transtorno depressivo. O serviço de sistema especialista não é um substituto de um profissional treinado, não dispensa a ajuda de um.
 
Alunos participantes do projeto: Eduardo Brasil Araújo e Rayssa M. Roseno.
 
## Como executar a aplicação
 
Como o programa foi escrito totalmente em python nativo, basta executar o arquivo `main.py` com o comando `python`, ou local do executável **python** para executar o programa e seguir as instruções impressas no terminal.
 
Exemplo de execução do programa:
`python main.py`
 
## Finalidade do projeto
 
Vimos que existem certos grupos de pessoas que possuem determinados transtornos mentais e não sabem a quem recorrer, ou quais serviços solicitar, portanto decidimos criar um sistema que automaticamente cria uma experiência customizada de recomendação que busca sanar, justamente, os problemas que os usuários estão enfrentando.
 
O principal objetivo do projeto é realizar um diagnóstico de algum transtorno mental, e prover das devidas orientações para o usuário. O trabalho de sistema especialista tem o propósito de executar um diagnóstico bem aproximado dos seguintes transtornos mentais:
* Depressão
* Ansiedade
 
O serviço de diagnóstico deverá ser respondido pelo usuário que está executando o programa, e todas as perguntas deverão ser respondidas em linguagem natural ou com o correspondente valor numérico da resposta. As perguntas deverão ser respondidas com: sim, talvez ou não, ou com a posição da resposta no campo de respostas (ver na saída do programa).
 
## Metodologia
 
O projeto de inteligência artificial baseado em um sistema especialista, é escrito em **python**. O projeto é escrito completamente nativo em python e utiliza módulos extras somente para manipulação de bytes string simples.
 
Escolhemos a linguagem de programação python por acreditarmos ser uma linguagem mais especializada para esse tipo de aplicação, por possuir mais frameworks e bibliotecas especializadas para essas aplicações específicas.
 
Para facilitar o processo de implementação, decidimos por criar um novo formato de arquivo em que se possa adicionar mais valores para certos transtornos que queiramos.
 
O formato de arquivo é um formato de texto simples (ASCII), para que possa ser mais facilmente modificado no decorrer do desenvolvimento, e tem como propósito a modularidade da implementação e de, possivelmente, adicionar novos transtornos de uma maneira mais facilitada.
 
## Novo formato de arquivo
 
Também foi criado um formato de arquivo para a implementação dos dados que queremos aplicar no sistema especialista. Basicamente existem os tipos de linhas que se podem ter no trabalho; cada linha tem um caráter que define o tipo da linha, entre eles:
* [`#`] - o primeiro é a linha do nome do transtorno
    * A linha que contém o nome do transtorno, e que, após ele, contém os parâmetros do transtorno que serão descritos
* [`?`] - O segundo é a linha de pergunta 
    * Contém as perguntas que serão impressas na tela para que o usuário possa responder
* [`<`] - o terceiro é a linha de parâmetros 
    * São os parâmetros que os usuários poderão entrar como resposta. 
    * Nela devem ser postas os valores ASCII, podendo ser unicode, e o valor inteiro que a resposta dada irá assumir.
* [`[`] - é a linha de alcance de cada grau do transtorno
    * Começa com '[' e contém dois números separados por vírgula indicando o alcance de determinado grau do transtorno, logo após um ']' para finalizar
    * Depois dos parâmetros de alcance, deve-se indicar o nome do grau em que a doença se enquadra
* [`!`] - o quinto é a descrição de recomendação para cada grau
    * Podem existir mais de uma linha de descrição em um mesmo alcance, porém deve-se iniciar a linha sempre com um "!", e não podem haver linhas em branco entre eles
    * É nele em que se coloca a descrição da recomendação caso o usuário seja diagnosticado com certo grau do transtorno
    * Essa classificação existe para que possamos adicionar uma customização à mais para o tipo de resultado obtido
* [`*`] - o campo de transtorno deve ser finalizado com um '*' asterisco, para indicar ao programa que os parâmetros devem ser aplicados à declaração do campo
* [` `] - o programa também tem a capacidade de finalizar um campo de transtorno com uma linha em branco, ao finalizar o arquivo ou ao pular da finalização de um campo de transtorno à outro
 
O programa em si não é um leitor deste formato específico, ou framework, por assim dizer, ele foi simplesmente escrito para uma mais fácil utilização dos tipos de perguntas que queríamos implementar e para a diminuição do código fonte em Python. Portanto, a má escrita de um banco de dados utilizando as especificações descritas anteriormente não serão tratadas como erros, mas gerará complicações na execução do programa, logo é necessário que se atenham às especificações atentamente, pois o programa não avisará caso esteja algo errado.
 
## Exemplos de entrada e saída
 
Ao executar o programa, nos deparamos com a mensagem de boas vindas:
 
```
O sistema especialista realiza o diagnóstico do Transtorno de Ansiedade e Transtorno Depressivo. O intuito é dar recomendações básicas acerca dos diagnósticos obtidos para que o usuário possa realizar as primeiras providências para sanar os problemas.
 
O usuário deverá responder as perguntas com os valores que estão entre parênteses, sendo eles em texto natural, como "sim" ou "Não", como também no valor da posição da resposta, como no caso do "não", que está na posição 0, logo, quando o usuário digitar 0 como resposta estará respondendo também com o valor "Não".
*Note que o programa não sabe diferenciar entre minúsculas, maiúsculas e letras com acentos*
 
 
Sinto que gosto de fazer as mesmas coisas de antes
<0 - Não, 1 - Talvez, 2 - Sim>
 
```
 
E, com a entrada de usuário todas com o valor 1 (que se traduz no valor 'Talvez'), temos a saída:
 
```
Ficamos muito felizes por você se encontrar com a saúde mental em dia, mas não deixe de sempre exercer em mantê-la, principalmente nos últimos tempos de pandemia.
 
Para depressão:
O CVV – Centro de Valorização da Vida tem como objetivo realizar apoio emocional e prevenção do suicídio, atendendo voluntária e gratuitamente todas as pessoas que querem e precisam conversar, sob total sigilo por telefone, email e chat 24 horas todos os dias.
acesse: https://www.cvv.org.br/
App Lojong: o App tem o objetivo exercícios para ajudar a controlar a ansiedade, aliviar o estresse, melhorar o foco, o sono e viver com mais felicidade.
acesse: https://play.google.com/store/apps/details?id=br.com.lojong&hl=pt_BR&gl=US
 
Para ansiedade e Depressão:
Serviço de Acolhimento Psicológico, Proest:
Consiste no acolhimento de estudantes por psicólogos da Pró-reitoria Estudantil Serviço de Acolhimento Psicológico
Acolhimento de estudantes por psicólogos da Pró-reitoria Estudantil (Proest) para orientação ou possível encaminhamento para rede SUS
acesse: https://servicos.ufal.br/orgaos/pro-reitoria-estudantil-proest/servico-de-acolhimento-psicologico
 
 
Lembre-se que essas soluções não substituem o tratamento real, procure sempre ajuda!
```
 
## Referências
* [Teste de tristeza ou depressão](https://neaar.org/como-saber-se-e-tristeza-ou-depressao-2475)
* [Teste de TAG](https://psicologafabiola.com.br/teste-tag-transtorno-de-ansiedade-generalizada/)
* [Aplicativo para meditação](https://play.google.com/store/apps/details?id=br.com.lojong&hl=pt_BR&gl=US)
* [Centro de suporte à vida](https://www.cvv.org.br/)
* [Serviço de acolhimento psicológico](https://servicos.ufal.br/orgaos/pro-reitoria-estudantil-proest/servico-de-acolhimento-psicologico)
 
 
 
 
 
