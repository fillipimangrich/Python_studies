lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite: o úmero que deseja adicionar à lista: '))
    lista.append(n)
    t = input('Deseja continuar? s/n ').lower()
    if t == 'n':
        break
for i in lista:
    if i%2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)
print(f'a lista com todos os elementos: {lista}')
print(f'a lista par é: {listapar}')
print(f'a lista impar é: {listaimpar}')