from itertools import count


n =  [int(x) for x in input('Digite 4 numeros separados por espaços:' ).split()]
n9 = n.count(9)
lista= []
for c in n:
    if c%2 == 0:
        lista.append(c)

print(f'O numero 9 aparaceu {n9} vezes')
if 3 not in n:
    print('O número 3 não esta na tupla')
else:
    n3 = n.index(3)+1
    print(f'O numero 3 aparece na posição {n3}')
print(f'Os numeros pares são: {lista}')