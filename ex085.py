lista = [list(),list()]
for i in range(1,8):
    n = int(input(f'Digite o {i}° valor: '))
    if n%2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'A lista dos números pares é: {lista[0]}')
print(f'A lista dos números ímpares é: {lista[1]}')