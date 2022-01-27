n = int(input('Qual seu salário?'))
v = int(input('Qual o valor da casa?'))
t = int(input('Em quantos anos quer pagar?'))
print(f'A prestação será de {v/(t*12)}')
if v/(t*12) > 0.3*n:
    print('Você não pode pegar emprestimo')
else:
    print('Você pode pegar o emprestimo')