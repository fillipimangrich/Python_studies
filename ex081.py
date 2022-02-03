lista = []
while True:
    n = int(input('Digite o número que deseja adicionar na lista:'))
    lista.append(n)
    t = input('Deseja continuar? s/n ').lower()
    if t == 'n':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort()
novalista = lista[::-1]
print(f'A lista invertida é: {novalista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')