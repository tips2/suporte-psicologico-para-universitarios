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

from unidecode import unidecode

def comp_str(string: str):
    return unidecode(string.lower())

class Disturbance:
    
    def __init__(self, name, questions, values, ranges):
        self.name = name
        self.questions = questions[:]
        self.values = values[:]
        self.ranges = ranges[:]
        self.score = 0

    def print(self):
        print(self.name)
        for quest in self.questions:
            print(quest)
        for value in self.values:
            print(value)
        for range in self.ranges:
            print(range)

    def question(self):
        param_question = '<'
        number_values = ''
        for i, value in enumerate(self.values):
            number_values += str(i) + ' '
            param_question += str(i) + ' - ' + str(value[0]) + ', '
        param_question = param_question.strip(', ')
        param_question += '>\n'
        
        low_param_question = unidecode(param_question.lower())

        for question in self.questions:
            print(question)
            print(param_question)
            answer = '2'
            answer_not_good = True
            while answer_not_good:
                if answer in '< , - >':
                    answer = 'none'
                if answer in number_values:
                    answer = self.values[int(answer)][0]
                answer = unidecode(answer.lower())
                if answer in low_param_question:
                    answer_not_good = False
                else:
                    answer = input('Reposta inválida, tente novamente\n')
            index = [unidecode(s[0].lower()) for s in self.values]
            index = index.index(answer)
            self.score += self.values[index][1]
    


def parse_file(file_path: str) -> Disturbance:
    dists = []
    with open(file_path, encoding='utf-8') as fp:
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
                name = line.strip(' #')
            elif line[0] == '<':
                line.index('(')
                value_tokens = line.strip('<> ').split(', ')
                value_tokens = [s.strip(')').split('(') for s in value_tokens]
                value_tokens = [[s[0], int(s[1])] for s in value_tokens]
                # value_tokens = list(chain(*value_tokens))
                values = value_tokens
            elif line[0] == '[':
                range_tokens = line.strip('[ ').split('] ')
                rng_vals = (range_tokens[0].split(', '))
                rng_vals = [int(s) for s in rng_vals]
                range_tokens = [rng_vals, range_tokens[1]]
                ranges = range_tokens
            else:
                questions.append(line)

    return dists

if __name__ == '__main__':
    folder = parse_file('question-db.dat')
    for attr in folder:
        attr.question()
        print(attr.score)