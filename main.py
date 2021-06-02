from unidecode import unidecode
import sys

from FileProcessor import FileParser

def comp_str(string: str):
    return unidecode(string.lower())

if __name__ == '__main__':
    debug = False
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'debug':
            debug = True

    folder = FileParser(debug).parse_file('question-db.dat')

    for attr in folder:
        attr.routine()
    
    print('O diagnóstico é:')
    
    for attr in folder:
        attr.print_status()
    
    print('Recomenda-se que:')

    for attr in folder:
        attr.print_recomendation()