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
    
    print('\nFicamos muito felizes por você se encontrar com a saúde mental em dia, mas não deixe de sempre exercer em mantê-la, principalmente nos últimos tempos de pandemia.')
    if folder[0].score == 0 and folder[1].score == 0:
        folder[0].print_recomendation()
    for attr in folder:
        attr.print_recomendation()
    
    if folder[0].score >= 1 and folder[1].score >= 1:
        print('\nPara ansiedade e Depressão:\nServiço de Acolhimento Psicológico, Proest:\nConsiste no acolhimento de estudantes por psicólogos da Pró-reitoria Estudantil Serviço de Acolhimento Psicológico\nO que é?\nAcolhimento de estudantes por psicólogos da Pró-reitoria Estudantil (Proest) para orientação ou possível encaminhamento para rede SUS\nacesse: https://servicos.ufal.br/orgaos/pro-reitoria-estudantil-proest/servico-de-acolhimento-psicologico\n\n')
    
    print('Lembre-se que essas soluções não substituem o tratamento real, procure sempre ajuda!\n')