usuario = {}
usuario['nome']= input('Digite seu nome: ')
nasc = int(input('Digite o ano de nascimento: '))
usuario['ano']= 2022 - nasc
usuario['carteira']= int(input('Digite o numero da sua carteira de trabalho: (se não tiver digite 0) '))

if usuario['carteira'] != 0:
        contratado = int(input('Digite o ano em que foi contratado: '))
        usuario['contratado'] = contratado
        usuario['salario'] = float(input('DIgite seu salario: '))
    
print(f"{usuario['nome']} tem {usuario['ano']} anos de idade ", end='')
if usuario['carteira']==0:
    print('e não possui carteira de trabalho.')
else:
    print(f", trabalha a {2022-int(usuario['contratado'])} anos e vai se aposentar em {int(usuario['contratado'])+35}")
