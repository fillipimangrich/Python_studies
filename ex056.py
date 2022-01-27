total = 0
menos20 = 0
idadevelho = 0
for c in range(1,5):
    nome = input('Qual seu primeiro nome?')
    idade = int(input('Qual sua idade?'))
    sexo = int(input('Qual seu sexo? [1] masculino [2] feminino'))
    total += idade
    if sexo == 1 :
        velho = nome
        if idadevelho ==0:
            idadevelho = idade
        elif idade > idadevelho:
            velho = nome
            idadevelho = idade
    elif sexo == 2 and idade < 20:
        menos20 += 1

print(f'A média de idade é {total/4}')
print(f'O mais velho se chama {velho} e tem {idadevelho} anos')
print(f'{menos20} mulheres tem menos de 20 anos')
