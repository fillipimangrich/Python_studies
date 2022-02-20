import moedas

n = float(input('Digite o preço: '))

print(f'O dobro de {moedas.moeda(n)} é {moedas.moeda(moedas.dobro(n))}')
print(f'A metade de {moedas.moeda(n)} é {moedas.moeda(moedas.metade(n))}')
print(f'Aumentando 27% de {moedas.moeda(n)} temos: {moedas.moeda(moedas.aumentar(n,27))}')
print(f'Diminuindo 3.5% de {moedas.moeda(n)} temos: {moedas.moeda(moedas.diminuir(n,3.5))}')
