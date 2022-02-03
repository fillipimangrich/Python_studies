lista = []
for i in range(0,5):
    n = int(input('Digite o número que deseja adicionar:'))
    if i == 0 or n >= lista[i-1]:
        lista.append(n)
    else:
            for t in range(0,len(lista)):
                    if n < lista[t]:
                        lista.insert(t,n)
                        break
print(lista)
