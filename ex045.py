from random import randint
print('{:=^40}'.format(' jokempo '))
opcao = int(input('''Qual sua opção?
[1] pedra
[2] papel
[3] tesoura
'''))
pc = randint(1,3)
print(pc)
if opcao == 1 and pc == 1:
    print('empatou')
elif opcao == 1 and pc == 2:
    print('o pc ganhou')
elif opcao == 1 and pc == 3:
    print('Você ganhou')
elif opcao == 2 and pc == 1:
    print('Você ganhou')
elif opcao == 2 and pc == 2:
    print('Empatou')
elif opcao == 2 and pc == 3:
    print('O pc ganhou')
elif opcao == 3 and pc == 1:
    print('O pc ganhou')
elif opcao == 3 and pc == 2:
    print('Você ganhou')
elif opcao == 3 and pc == 3:
    print('empatou')
else:
    print('Selecione uma opção valida')
