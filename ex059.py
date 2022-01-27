n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n = 0
while n != 5:
    n = int(input('''O que você deseja fazer:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    '''))
    if n == 1:
        print(f'A soma é {n1+n2}')
    elif n == 2:
        print(f'A multiplicação é {n1*n2}')
    elif n ==3:
        if n1 > n2:
            print(f'{n1} é maior')
        elif n1 ==n2:
            print('São iguais')
        else:
            print(f'{n2} é maior')
    elif n ==4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif n != 5:
        print('escolha uma opção válida')

print('FIM')