n = int(input('Digite um número inteiro:'))
print('''escolha uma base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal
''')
op = int(input('Sua opção:'))
if op == 1:
    print(f'{n} em binário é {bin(n)[2:]}')
elif op == 2:
    print(f'{n} em octal é {oct(n)[2:]}')
elif op == 3:
    print(f'{n} em hexadecimal é {hex(n)[2:]}')
else:
    print('opção inválida!')