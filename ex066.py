soma = 0
c = 0
while True:
    n = int(input('Digite um valor: [999] para sair.'))
    if n == 999:
        break
    soma += n
    c += 1
print(f'Soma dos {c} valores é {soma}')

