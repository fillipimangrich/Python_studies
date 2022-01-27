n = 0
soma = 0
c = 0
while n != 999:
    n = int(input('Digite um numero:'))
    soma += n
    c += 1
print(f'Foram digitados {c} números e a soma entre eles é {soma}')