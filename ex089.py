lista = []
while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = int(input('Digite a nota 1: '))
    nota2 = int(input('Digite nota 2: '))
    media = (nota1 + nota2)/2
    lista.append([nome,[nota1, nota2], media])
    t = input('Deseja continuar cadastrando?: s/n ').lower()
    if t == 'n':
        break

for i in lista:
     print(f'{i[0]} tirou as notas {i[1]} e sua média foi {i[2]}')
    