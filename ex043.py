peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso/(altura**2)
if imc < 18.5:
    print('Você está magro demais!')
elif 18.5 < imc < 25:
    print('Seu peso está ideal')
elif 25 < imc < 30:
    print('Você está com sobrepeso')
elif 30 < imc < 40:
    print('Você está obeso')
elif imc > 40:
    print('você está com obsedidade mórbida')
