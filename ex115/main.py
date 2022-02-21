from lib import interface
from lib import arquivo

arq = 'cursoemvideo.txt'

if arquivo.arqexiste(arq):
    pass
else:
    print('Arquivo não encontrado')
    arquivo.criararq(arq)


interface.menu(['cadastrar pessoas','listar pessoas'])

