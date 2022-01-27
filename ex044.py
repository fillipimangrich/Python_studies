n = float(input('Qual o valor do produto?'))
m = int(input('''Qual o método de pagamento?
[1] Dinheiro/cheque
[2] À vista no cartão
[3] Até 2x no cartão
[4] 3x ou mais no cartão
'''))
if m == 1:
    print(f'no dinheiro/cheque esse produto custa {0.9*n} reais')
elif m == 2:
    print(f'À vista no cartão esse produto custa {0.95*n} reais')
elif m == 3:
    print(f'em 2x no cartão esse produto custa {n} reais')
elif m == 4:
    print(f'em 3x ou mais no cartão esse produto custa {n*1.2} reais')
else:
    print('selecione uma opção valida')
