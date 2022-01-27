p = 'S'
soma = 0
c = 0
while p == 'S':
    n = int(input('Digite um valor:'))
    soma += n
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c += 1
    p = (input('Quer continuar? [s] [n]')).upper()

print(f'Você digitou {c} números, a média deles foi {soma/c}, o maior foi {maior} e o menor {menor}.')