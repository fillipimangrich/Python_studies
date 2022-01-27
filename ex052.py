n = int(input('Digite um número:'))
d = 0
for c in range (2,n):
    if (n%c) == 0:
        d += 1
if d == 0:
    print('é primo')
else:
    print('Não é primo')
