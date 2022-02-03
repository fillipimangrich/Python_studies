lista = [list(), list() ,list()]
soma = 0
soma3 = 0
soma2 = 0
for i in range(0,3):
    for k in range(0,3):
        n = int(input(f'Digite o valor da posição {i,k}'))
        lista[i].append(n)
        soma += n
        if k == 2:
            soma3 += n
        if i == 1:
            soma2 += n
for i in lista:
    print(i)

print(f'A soma de todos os valores é : {soma}')
print(f'A soma de todos os valores da terceira coluna é {soma3}')
print(f'A soma de todos os valores da segunda linha é {soma2}')
