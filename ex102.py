def fatorial(n, mostrar = False):
    """
    -> Calcula o fatorial de um número.
    :param n: Valor na qual se deseja calcular o fatorial.
    :param mostrar: Habilita/Desabilita a exibição do procedimento.
    :return: sem retorno.
    """
    resultado = 1
    for i in range(1,n+1):
        resultado *= i
    if mostrar == True:
        for i in range(n,1,-1):
            print(f'{i}*', end='')
        print(f'1 = {resultado}')

    else:
        print(resultado)

n = int(input('Qual valor você deseja saber o fatorial? '))

fatorial(n, mostrar = True)
help(fatorial)