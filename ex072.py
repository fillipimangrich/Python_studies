número = ('um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = 0
while True:
    n = int(input('Digite um número de 1 a 20:'))
    if n > 20 or n <1:
        print('Digite um número válido')
    else:
        break
print(f'Você escolheu o número {número[n-1]}')