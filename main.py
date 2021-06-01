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

class Disturbance:
    
    def __init__(self, name, questions, values, ranges):
        self.name = name
        self.questions = questions[:]
        self.values = values[:]
        self.ranges = ranges[:]

    def print(self):
        print(self.name)
        for quest in self.questions:
            print(quest)
        for value in self.values:
            print(value)
        for range in self.ranges:
            print(range)

def parse_file(file_path: str):
    dists = []
    with open(file_path) as fp:
        name = ''
        questions = []
        values = []
        ranges = []

        for line in fp:
            line = line.strip()
            if line == '*':
                dist = Disturbance(name, questions, values, ranges)
                dists.append(dist)
                name = ''
                questions.clear()
                values.clear()
                ranges.clear()
            elif line[0] == '#':
                name = line[1:].strip()
            elif line[0] == '<':
                line.index('(')
                value_tokens = line.strip('<> ').split(', ')
                value_tokens = [s.strip(')').split('(') for s in value_tokens]
                value_tokens = [[s[0], int(s[1])] for s in value_tokens]
                values.append(value_tokens)
            elif line[0] == '[':
                range_tokens = line.strip('[ ').split('] ')
                # range_tokens = [s.split(', ') for s in range_tokens]
                rng_vals = (range_tokens[0].split(', '))
                rng_vals = [int(s) for s in rng_vals]
                range_tokens = [rng_vals, range_tokens[1]]
                ranges.append(range_tokens)
            else:
                questions.append(line)

    return dists

if __name__ == '__main__':
    folder = parse_file('question-db.dat')
    for attr in folder:
        attr.print()
