idade = 0
sexo = 0
c = 0
homens = 0
mulheres_20 = 0

while True:
    n = input('Digite a idade: ')
    sexo = input('Digite o sexo:[f][m]').lower()
    if idade > 18:
        c+=1
    if sexo == 'h':
        homens += 1
    if idade<20 and sexo =='f':
        mulheres_20 +=1
    if input('Quer continuar? [s] [n]') == 'n':
        break
print(f'{c} pessoas tem mais do que 18 anos, {homens} são homens e {mulheres_20} são mulheres com menos de 20 anos.')