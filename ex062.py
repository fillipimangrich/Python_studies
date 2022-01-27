first = int(input('Qual o primeiro numero?'))
q = int(input('Qual a razão?'))
n = 0
while n<10:
    print(f'{first}')
    first += q
    n += 1
c = 1
t = 0
while c !=0 :
    c = int(input('Quer mostrar mais quantos termos?'))
    while t != c:
        print(f'{first}')
        first += q
        t += 1
    t = 0
print('Fim!')