from unidecode import unidecode
import sys

from FileProcessor import FileParser

if __name__ == '__main__':
    debug = False
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'debug':
            debug = True

    folder = FileParser(debug).parse_file('question-db.dat')

    for attr in folder:
        attr.routine()
        
    for attr in folder:
        attr.print_status()
    
    for attr in folder:
        attr.print_recomendation()