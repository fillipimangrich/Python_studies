from random import randint
escolha = input('VocÊ quer par ou impar?[digite par ou impar]').lower()
n = 0
pc = 0
soma = 0
c = 0
while True:
    n = int(input('Digite um número: '))
    pc = randint(0,10)
    soma = pc+n
    if escolha == 'par':
        if soma%2 == 0:
            print('Você ganhou!')
            c += 1
        else:
            print(f'Você perdeu e teve {c} vitórias seguidas.')
            break
    else:
        if soma%2 != 0:
            print('Você ganhou!')
            c += 1
        else:
            print(f'Você perdeu e teve {c} vitórias seguidas.')
            break