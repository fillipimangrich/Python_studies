from lib import arquivo

arq = 'cursoemvideo.txt'


def linha(tam = 50):
    return '-'*tam



def cabeçalho(txt):
    print(linha())
    print(f'|{txt:^48}|')
    print(linha())

def menu(lista):
    while True:
        cabeçalho('MENU PRINCIPAL')
        for k,c in enumerate(lista):
            n = f'{k+1} - {c}'
            print(f'|{n:^48}|')
        sair = 'DIGITE 0 PARA SAIR'
        print(f'|{sair:^48}|')
        option = leiaint('Selecione a opção: ')
        while True:
            if option not in [0,1,2]:
                print('Digite uma opção válida!')
                option = leiaint('Selecione a opção: ')
            else: break
        if option == 1:
            nome = input('Digite o nome: ')
            idade = leiaint('Digite a idade: ')
            arquivo.cadastrar(arq, nome, idade)
        elif option == 2:
            arquivo.lerarquivo(arq)
        elif option == 0:
            agradecimento = 'OBRIGADO, VOLTE SEMPRE!'
            print(f'|{agradecimento:^48}|')
            break


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
            break
        except:
            print('Error, digite somente números interios!')


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
            break
        except:
            print('Error, digite somente numeros reais!')



