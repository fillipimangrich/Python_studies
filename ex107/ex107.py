import moedas

n = float(input('Digite o preço: '))

print(f'O dobro de {n} é {moedas.dobro(n)}')
print(f'A metade de {n} é {moedas.metade(n)}')
print(f'Aumentando 27% de {n} temos: {moedas.aumentar(n,27)}')
print(f'Diminuindo 3.5% de {n} temos: {moedas.diminuir(n,3.5)}')
