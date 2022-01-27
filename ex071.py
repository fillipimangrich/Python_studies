
n50 = 0
n20 = 0
n10 = 0
n1 = 0
n = int(input('Quanto você quer sacar?'))

n50 = n//50
resto50 = n%50
n20 = resto50//20
resto20 = resto50%20

n10 = resto20//10
resto10 = resto20%10
n1 = resto10

print(f'Você recebeu {n50} notas de 50 {n20} notas de 20 {n10} notas de 10 e {n1} notas de 1')

