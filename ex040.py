n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
if media >= 6:
    print('Você está aprovado')
elif media < 6 and media >= 5:
    print('Você está de recuperação')
else:
    print('Você está reprovado')
