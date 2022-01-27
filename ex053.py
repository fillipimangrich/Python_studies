p = str(input('Digite uma frase:')).lower().replace(' ','')
if p == p[::-1]:
    print('é um palidromo')
else:
    print('não é um palindromo')

