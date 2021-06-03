from unidecode import unidecode

class Disturbance:
    
    def __init__(self, name, questions, values, ranges, recomend, debug = False):
        self.name = name
        self.questions = questions[:]
        self.values = values[:]
        self.ranges = ranges[:]
        self.recomend = recomend[:]
        self.score = 0
        self.debug = debug

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
            if not self.debug:
                answer = input(question + '\n' + param_question)
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
        print(f'{self.name} {self.disturb_status}')

    def print_recomendation(self):
        print('\n' + self.recomend[self.status_index])
        # for i in self.recomend[0:self.status_index]:
        #     if i != '':
        #         print(i)