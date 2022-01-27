n = int(input('Digite quantos numeros da sequencia você quer:'))
c = 0
n1 = 0
n2 = 1
while c <= n:
    print(n1, end=' - ')
    n2 += n1
    n1 = n2 - n1
    c += 1

