def leiaint(n):
    while True:
        numero = input(n)
        if not numero.isnumeric():
            print('Digite um número!')
        else:
            numero = int(numero)
            return numero
            break
n = leiaint('Digite um numero:')
print(f'Você digitou o numero {n}')