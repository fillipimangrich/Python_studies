from datetime import date
n = int(input('Qual seu ano de nascimento:'))
hj = date.today().year
idade = hj - n
print(f'o atleta tem {idade} anos')
if idade < 8:
    print('Classificação: mirim')
elif 7 < idade < 14:
    print('Classificação: infantil')
elif 14 < idade < 19:
    print('Classificação: juvenil')
elif 19 < idade < 25:
    print('Classificação: sênior')
elif idade > 25:
    print('Classificação: Master')

