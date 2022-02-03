lista = [list(), list() ,list()]
for i in range(0,3):
    for k in range(0,3):
        n = int(input(f'Digite o valor da posição {i,k}'))
        lista[i].append(n)
for i in lista:
    print(i)