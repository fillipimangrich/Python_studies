def ajuda(n):

    help(n)

while True:
    print('Bem vindo ao pyhelp!')
    n = input('Função ou biblioteca: ')
    if n == 'fim':
        break
    ajuda(n)
