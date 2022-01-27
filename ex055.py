maior = 0
menor = 0

for c in range(1,6):
    p = float(input('Qual seu peso?'))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print(f'O maior é {maior}')
print(f'O menor é {menor}')

