def aumentar(n,x):
    novo_valor = n * (1+(x/100))
    return novo_valor

def diminuir(n,x):
    novo_valor = n * (1-(x/100))
    return novo_valor

def dobro(n):
    novo_valor = n*2
    return novo_valor

def metade(n):
    novo_valor = n/2
    return novo_valor

def moeda(n):
    n = f'R${n}'
    return n