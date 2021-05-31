'''
Basicamente se utilizam duas bibliotecas para desenvolver
o projeto: a biblioteca panda para poder ler e interpretar
o arquivo da base de dados csv, e a biblioteca sklearn, que
é responsável por criar o modelo da árvore de decisões.

Primeiramente se abre o arquivo da base de dados com o módulo
panda que será responsvável pela vizualização da base de dados,
depois se definirá qual o vetor de alvos que será a reposta que
pretendemos alcançar.

O comando 'drop' serve para tirar determinados valores do arquivo
csv, e o valor "axis='column'" significa que irá remover todos os
valores do eixo vertical do arquivo. Os dados são acessados por
um hashmap que toma como parâmetro o valor do nome da coluna.

Depois de separado os valores paramétricos dos valores de alvo,
se realiza a codificação dos parâmetros, que transforma os valores
em texto para valores numéricos que são mais fáceis de serem
trabalhados pelo programa. Para isso, utiliza-se do submódulo
preprocessing da biblioteca sklearn, com a função LabelEncoder.

LabelEncoder().fit_transform(<name of column to encode>)

Então, com os dados codificados, instancia-se uma árvore de 
classificação por decisão e coloca-se os valores que obtivermos
até então como primeiro argumento, e como segundo argumento, o
vetor de alvo que se obteve no início.

Para verificar algum alvo arbitrário, basta chamar a função
predict da árvore e colocar os valores arbitrários como parâmetros.
'''

def start() -> float:
    print('This is the start function')

if __name__ == '__main__':
    print('hello world')
    start()