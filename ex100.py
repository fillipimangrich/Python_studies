from random import randint

def sorteio(lista): 
    for i in range (0,5):
        n = randint(0,100)
        lista.append(n)
    print(lista)
    

def soma(lista):
    somatotal = 0
    for i in lista:
        if i % 2 == 0:
            somatotal += i
    print(f'A soma dos números pares é {somatotal} ')

n = []
sorteio(n)
soma(n)