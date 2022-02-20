import moeda
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

def resumo(n,x,y):
    print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n,True)}')
    print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n,True)}')
    print(f'Aumentando 27% de {moeda.moeda(n)} temos: {moeda.aumentar(n,27,True)}')
    print(f'Diminuindo 3.5% de {moeda.moeda(n)} temos: {moeda.diminuir(n,3.5,True)}')