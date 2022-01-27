from random import randint
n = randint(1,10)
palpite = 0
tentativa = 0
while palpite != n:
    palpite = int(input('Digite um palpite: '))
    tentativa += 1
print(f'Você acertou! Forem necessárias {tentativa} tentativas!')
