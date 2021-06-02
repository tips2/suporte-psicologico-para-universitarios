from unidecode import unidecode
import sys

debug = False

def comp_str(string: str):
    return unidecode(string.lower())

class Disturbance:
    
    def __init__(self, name, questions, values, ranges, recomend):
        self.name = name
        self.questions = questions[:]
        self.values = values[:]
        self.ranges = ranges[:]
        self.recomend = recomend[:]
        self.score = 0

    def print(self):
        print(self.name)
        for quest in self.questions:
            print(quest)
        for value in self.values:
            print(value)
        for range in self.ranges:
            print(range)

    # This method prompts the user all the questions of the disturbance,
    # also requires an answer from the user
    def question(self):
        param_question = '<'
        number_values = ''
        for i, value in enumerate(self.values):
            number_values += str(i) + ' '
            param_question += str(i) + ' - ' + str(value[0]) + ', '
        param_question = param_question.strip(', ')
        param_question += '>\n'
        
        low_param_list = [unidecode(s[0].lower()) for s in self.values]

        for question in self.questions:
            print(question)
            global debug
            if not debug:
                answer = input(param_question)
            else:
                answer = '2'
            answer_not_good = True
            answer = answer.strip(' \r\n')
            while answer_not_good:
                if answer in '< , - >':
                    answer = 'none'
                if answer in number_values:
                    answer = self.values[int(answer)][0]
                answer = unidecode(answer.lower())
                if answer in low_param_list:
                    answer_not_good = False
                else:
                    answer = input('Reposta inválida, tente novamente\n')
            index = low_param_list.index(answer)
            self.score += self.values[index][1]
    
    # This method fits the score gotten into the ranges from the db
    def fit_param(self):
        for i, [[first, second], word] in enumerate(self.ranges):
            if self.score >= first and self.score <= second:
                self.disturb_status = word
                self.status_index = i
                break

    def routine(self):
        self.question()
        self.fit_param()
    
    def print_status(self):
        print(f'{self.name}: {self.disturb_status}')

    def print_recomendation(self):
        for i in self.recomend[self.status_index:-1]:
            if i != '':
                print(i)

class FileParser:
    def finalization(self, line: str) -> None:
        dist = Disturbance(
            self.name, self.questions, self.values, self.ranges, self.recomend
        )
        self.dists.append(dist)
        self.name = ''
        self.questions.clear()
        self.values.clear()
        self.ranges.clear()
        self.recomend.clear()

    def naming(self, line: str) -> None:
        self.name = line.strip(' #')

    def tokening(self, line: str) -> None:
        line.index('(')
        value_tokens = [s.strip(' ') for s in line.strip('<> ').split(',')]
        value_tokens = [s.strip(')').split('(') for s in value_tokens]
        value_tokens = [[s[0], int(s[1])] for s in value_tokens]
        self.values = value_tokens

    def rangening(self, line: str) -> None:
        range_tokens = line.strip('[ ').split('] ')
        rng_vals = [s.strip(' ') for s in range_tokens[0].split(',')]
        rng_vals = [int(s) for s in rng_vals]
        range_tokens = [rng_vals, range_tokens[1]]
        self.ranges.append(range_tokens)

    def questioning(self, line: str) -> None:
        self.questions.append(line.strip('? '))

    def recomendation(self, line: str) -> None:
        self.recomend.append(line.strip('! '))

    def parse_file(self, file_path: str) -> Disturbance:
        self.dists = []
        with open(file_path, encoding='utf-8') as fp:
            self.name = ''
            self.questions = []
            self.values = []
            self.ranges = []
            self.recomend = []

            switchers = {
                '*': self.finalization,
                '#': self.naming,
                '<': self.tokening,
                '[': self.rangening,
                '?': self.questioning,
                '!': self.recomendation
            }

            for line in fp:
                line = line.strip()
                switchers[line[0]](line)

        return self.dists

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'debug':
            debug = True

    folder = FileParser().parse_file('question-db.dat')

    for attr in folder:
        attr.routine()
    
    print('O diagnóstico é:')
    
    for attr in folder:
        attr.print_status()
    
    print('Recomenda-se que:')

    for attr in folder:
        attr.print_recomendation()