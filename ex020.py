import random
n1 = input('Digite o primeiro aluno:')
n2 = input('Digite o segundo aluno:')
n3 = input('Digite o terceiro aluno:')
n4 = input('Digite o ultimo aluno:')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentação é: {lista}')
