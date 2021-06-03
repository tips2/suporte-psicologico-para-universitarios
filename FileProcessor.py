from DisturbanceClass import Disturbance
from enum import Enum, auto

class line_type(Enum):
    none = auto()
    end = auto()
    name = auto()
    token = auto()
    range = auto()
    description = auto()
    question = auto()

class FileParser:
    def __init__(self, debug = False):
        self.instance = False
        self.debug = debug
        self.in_range = False
        self.rec_lines = ''

    def finalization(self, line: str) -> None:
        if not self.instance:
            return 
        self.instance = False
        for _ in range(len(self.recomend), len(self.ranges)):
            self.recomend.append('')
        
        dist = Disturbance(
            self.name, self.questions, self.values, self.ranges, self.recomend, self.debug
        )
        self.dists.append(dist)
        self.name = ''
        self.questions.clear()
        self.values.clear()
        self.ranges.clear()
        self.recomend.clear()

    def naming(self, line: str) -> None:
        self.instance = True
        self.name = line.strip(' #')

    def tokening(self, line: str) -> None:
        line.index('(')
        value_tokens = [s.strip(' ') for s in line.strip('<> ').split(',')]
        value_tokens = [s.strip(')').split('(') for s in value_tokens]
        value_tokens = [[s[0], int(s[1])] for s in value_tokens]
        self.values = value_tokens

    def rangening(self, line: str) -> None:
        self.in_range = True
        range_tokens = line.strip('[ ').split('] ')
        rng_vals = [s.strip(' ') for s in range_tokens[0].split(',')]
        rng_vals = [int(s) for s in rng_vals]
        range_tokens = [rng_vals, range_tokens[1]]
        self.ranges.append(range_tokens)

    def recomendation(self, line: str) -> None:
        if not self.in_range:
            raise Exception("Need to have a range line before description")
        for _ in range(len(self.recomend), len(self.ranges) - 1):
            self.recomend.append('')
        self.rec_lines += line.strip('! ') + '\n'

    def questioning(self, line: str) -> None:
        self.questions.append(line.strip('? '))

    def parse_file(self, file_path: str) -> Disturbance:
        self.dists = []
        self.instance = False
        with open(file_path, encoding='utf-8') as fp:
            self.name = ''
            self.questions = []
            self.values = []
            self.ranges = []
            self.recomend = []

            switchers = {
                '#': self.naming,
                '<': self.tokening,
                '[': self.rangening,
                '?': self.questioning,
                '!': self.recomendation,
                '*': self.finalization,
            }

            for line in fp:
                line = line.strip()
                if line == '':
                    func = self.finalization
                else:
                    func = switchers[line[0]]

                if self.in_range and func != self.recomendation:
                    self.recomend.append(self.rec_lines.strip())
                    self.rec_lines = ''
                    self.in_range = False
                
                if self.instance and func == self.naming:
                    self.finalization('')

                func(line)

                if not self.in_range and func != self.recomendation:
                    self.in_range = False
            self.finalization('')
        return self.dists