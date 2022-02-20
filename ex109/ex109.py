import moedasplus

n = float(input('Digite o preço: '))

print(f'O dobro de {moedasplus.moeda(n)} é {moedasplus.dobro(n,True)}')
print(f'A metade de {moedasplus.moeda(n)} é {moedasplus.metade(n,True)}')
print(f'Aumentando 27% de {moedasplus.moeda(n)} temos: {moedasplus.aumentar(n,27,True)}')
print(f'Diminuindo 3.5% de {moedasplus.moeda(n)} temos: {moedasplus.diminuir(n,3.5,True)}')