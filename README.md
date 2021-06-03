# Suporte psicológico para alunos de exatas
 
Orientação para um semi-diagnóstico dos transtornos de ansiedade e transtorno depressivo. O serviço de sistema especialista não é um substituto de um profissional treinado, não dispense a ajuda de um.
 
Alunos participantes do projeto: Eduardo Brasil Araújo e Rayssa M. Roseno.
 
## Metodologia
 
O projeto de inteligência artificial baseado em um sistema especialista, é escrito em **python**. O projeto é escrito completamente nativo em python utilizando módulos extras somente para manipulação de bytes string simples.
 
Também foi criado um formato de arquivo para a implementação dos dados que queremos aplicar no sistema especialista. Basicamente existem os tipos de linhas que se podem ter no trabalho; cada linha tem um caráter que define o tipo da linha, entre eles:
* [`#`] - o primeiro é a linha do nome do transtorno
    * A linha que contém o nome do transtorno, e que, após ele, contém os parâmetros do transtorno que serão descritos
* [`?`] - O segundo é a linha de pergunta 
    * Contém as perguntas que serão impressas na tela para que o usuário possa responder
* [`<`] - o terceiro é a linha de parâmetros 
    * São os parâmetros que os usuários poderão entrar como resposta. 
    * Nela devem ser postas os valores ascii, podendo ser unicode, e o valor inteiro que a resposta dada irá assumir.
* [`[`] - é a linha de alcance de cada grau do transtorno
    * Começa com '[' e contém dois números separados por vírgula indicando o alcance de determinado grau do transtorno, logo após um ']' para finalizar
    * Depois dos parâmetros de alcance, deve-se indicar o nome do grau em que a doença se enquadra
* [`!`] - o quinto é a descrição de recomendação para cada grau
    * É indispensável que exista esse campo na implementação atual, e que exista um campo para cada alcance especificado
    * É nele em que se coloca a descrição da recomendação caso o usuário seja diagnosticado com certo grau do transtorno
    * Essa classificação existe para que possamos adicionar uma customização à mais para o tipo de resultado obtido
* [`*`] - o campo de transtorno deve ser finalizado com um '*' asterisco, para indicar ao programa que os parâmetros devem ser aplicados à declaração do campo
 
A finalidade da criação do formato é a de simplificar a implementação de múltiplos transtornos, e, podendo ser utilizada, posteriormente, para sistemas especialistas mais abrangentes envolvendo diagnóstico rápido de transtornos mentais.
 
O programa em si não é um leitor deste formato específico, ou framework, por assim dizer, ele foi simplesmente escrito para uma mais fácil utilização dos tipos de perguntas que queríamos implementar e para a diminuição do código fonte em Python. Portanto, a má escrita de um banco de dados utilizando as especificações descritas anteriormente não serão tratadas como erros, mas gerará complicações na execução do programa, logo é necessário que se atenham às especificações atentamente, pois o programa não avisará caso esteja algo errado.
 
Escolhemos a linguagem de programação python por acreditarmos ser uma linguagem mais especializada para esse tipo de aplicação, por possuir mais frameworks e bibliotecas especializadas para essas aplicações específicas.
 
O principal objetivo do projeto é realizar um diagnóstico de algum transtorno mental, o trabalho de sistema especialista tem o propósito de realizar um diagnóstico bem aproximado dos seguintes transtornos mentais:
* Depressão
* Ansiedade
 
O serviço de diagnóstico deverá ser respondido pelo usuário que está executando o programa, e todas as perguntas deverão ser respondidas em linguagem natural ou com o correspondente valor numérico da resposta. As perguntas deverão ser respondidas com: sim, talvez ou não. Cada valor terá a intensidade do grau do transtorno.
 
## Referências
* [Machine Learning Tutorial Python - 9 Decision Tree](https://www.youtube.com/watch?v=PHxYNGo8NcI)
* https://play.google.com/store/apps/details?id=br.com.lojong&hl=pt_BR&gl=US
* https://www.cvv.org.br/
* https://servicos.ufal.br/orgaos/pro-reitoria-estudantil-proest/servico-de-acolhimento-psicologico
