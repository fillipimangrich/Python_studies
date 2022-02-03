lista = []
while True:
    n = int(input('Digite o valor que deseja adicionar na lista:'))
    if n in lista:
        c = input('Valor duplicado, deseja continuar? s/n ')
        if c == 'n':
            break
    else:
        lista.append(n)
        t = input('Valor adicionado, deseja continuar? s/n ')
        if t == 'n':
            break
lista.sort
print(lista)
