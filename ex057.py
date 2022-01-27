s = ''
while s != 'M'and s != 'F':
    s = input('Qual seu sexo?[M,F]').upper()
    if s != 'M' and s!='F':
        print('Digite uma opção valida')
print('Fim')