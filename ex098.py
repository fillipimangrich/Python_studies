def contagem(inicio, fim, passo):
    if inicio > fim:
        fim -= 1
    elif fim > inicio:
        fim += 1
    for i in range(inicio,fim,passo):
        print(i)

contagem(1,10,1)
print()
contagem(10,0,-2)
a,b,c = [int(x) for x in input('Digite o inicio, o fim e o passo separado por espaços:').split()]
contagem(a,b,c)
