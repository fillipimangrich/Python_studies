def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
            break
        except:
            print('Error, digite somente números interios!')
            

    

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
            break
        except:
            print('Error, digite somente numeros reais!')
            

i = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número real: ')

print(f'você digitou os numeros: {i} e {r}')