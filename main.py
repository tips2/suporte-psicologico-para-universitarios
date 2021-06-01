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
    
    # This method fits the score gotten into the ranges from the db
    def fit_param(self):
        for [first, second], word in self.ranges:
            if self.score >= first and self.score <= second:
                self.disturb_status = word
                break

    def routine(self):
        self.question()
        self.fit_param()
    
    def print_status(self):
        print(self.disturb_status)

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
                value_tokens = [s.strip(' ') for s in line.strip('<> ').split(',')]
                value_tokens = [s.strip(')').split('(') for s in value_tokens]
                value_tokens = [[s[0], int(s[1])] for s in value_tokens]
                # value_tokens = list(chain(*value_tokens))
                values = value_tokens
            elif line[0] == '[':
                range_tokens = line.strip('[ ').split('] ')
                rng_vals = [s.strip(' ') for s in range_tokens[0].split(',')]
                rng_vals = [int(s) for s in rng_vals]
                range_tokens = [rng_vals, range_tokens[1]]
                ranges.append(range_tokens)
            else:
                questions.append(line)

    return dists

if __name__ == '__main__':
    folder = parse_file('question-db.dat')
    for attr in folder:
        attr.routine()
    
    for attr in folder:
        print(f'Se retratando de {attr.name}: ', end='')
        attr.print_status()