def aumentar(n,x,formatar = False):
    novo_valor = n * (1+(x/100))
    if formatar:
        novo_valor = f'R${novo_valor}'
    return novo_valor

def diminuir(n,x,formatar = False):
    novo_valor = n * (1-(x/100))
    if formatar:
        novo_valor = f'R${novo_valor}'
    return novo_valor

def dobro(n,formatar = False):
    novo_valor = n*2
    if formatar:
        novo_valor = f'R${novo_valor}'
    return novo_valor

def metade(n,formatar = False):
    novo_valor = n/2
    if formatar:
        novo_valor = f'R${novo_valor}'
    return novo_valor

def moeda(n):
    n = f'R${n}'
    return n