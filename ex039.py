from datetime import date
n = int(input('Em qual ano você nasceu?'))
hj = date.today().year
data = n + 18
idade = hj - n
print(f'Quem nasceu em {n} tem {idade} anos em {hj}')
if idade > 18:
    print(f'Você deveria ter se alistado em {data}, há {hj - data} anos.')
elif idade == 18:
    print('Você deve ir se alistar esse ano')
else:
    print(f'Você vai se alistar em {data}, daqui {data - hj} anos.')