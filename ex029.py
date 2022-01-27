n = int(input('Qual a velocidade:'))
multa = (n - 100)*7
print(f'Você foi multado, e a multa é de {multa} reais') if n > 100 else print('Você não foi multado')
