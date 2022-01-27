cont = 0
for c in range (1,8):
    i = int(input('Qual sua idade?'))
    if i >= 21:
        cont +=1
print(f'{cont} pessoas são maiores de idade e {7-cont} não são.')

