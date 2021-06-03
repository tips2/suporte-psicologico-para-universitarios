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
        self.debug = debug
        self.previous = line_type.none

    def finalization(self, line: str) -> None:
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
        self.previous = line_type.end

    def naming(self, line: str) -> None:
        self.name = line.strip(' #')
        self.previous = line_type.name

    def tokening(self, line: str) -> None:
        line.index('(')
        value_tokens = [s.strip(' ') for s in line.strip('<> ').split(',')]
        value_tokens = [s.strip(')').split('(') for s in value_tokens]
        value_tokens = [[s[0], int(s[1])] for s in value_tokens]
        self.values = value_tokens
        self.previous = line_type.token

    def rangening(self, line: str) -> None:
        range_tokens = line.strip('[ ').split('] ')
        rng_vals = [s.strip(' ') for s in range_tokens[0].split(',')]
        rng_vals = [int(s) for s in rng_vals]
        range_tokens = [rng_vals, range_tokens[1]]
        self.ranges.append(range_tokens)
        self.previous = line_type.range

    def recomendation(self, line: str) -> None:
        if self.previous != line_type.range:
            raise Exception("Need to have a range line before description")
        for _ in range(len(self.recomend), len(self.ranges) - 1):
            self.recomend.append('')
        self.recomend.append(line.strip('! '))
        self.previous = line_type.description

    def questioning(self, line: str) -> None:
        self.questions.append(line.strip('? '))
        self.previous = line_type.question

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