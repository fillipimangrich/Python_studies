n1 = int(input('Digite a reta 1: '))
n2 = int(input('Digite a reta 2: '))
n3 = int(input('Digite a reta 3: '))
if n1 + n2 <= n3 or n1 + n3 <= n2 or n2 +n3 <= n1:
    print('\033[1;32;40mNão da pra formar um triangulo\033[m')
else:
    print('\033[1;97;41mDa pra formar um triangulo\033[m')

'''
text     background

30black  preto 40
31red    vermelho 41
32green  verde 42
33yellow amarelo 43
34blue   azul 44
35MagentaMagenta 45
36cyan   ciano 46
37grey   cinza 47
97white  branco 107
'''