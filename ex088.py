from random import randint

n = int(input('Quantos jogos você deseja criar? '))
lista = []

for i in range(0,n):
    lista.append(list())
    for k in range(0,6):
        while len(lista[i]) != 6:
            n = randint(1,61)
            if n not in lista[i]:
                lista[i].append(n)
    print(f'Jogo {i+1}: {lista[i]}')
