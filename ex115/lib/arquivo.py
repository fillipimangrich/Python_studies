from lib import interface


def arqexiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(nome):
    try:
        a= open(nome, 'wt+')
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado!')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        interface.cabeçalho('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'|{dado[0]:<40}{dado[1]:>3} anos|')
    finally:
        a.close()

def cadastrar(arq,nome = 'Desconhecido',idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um error ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Error ao escrever dados!')
        else:
            print('Novo cadastro adicionado!')
            a.close()