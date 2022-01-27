n = int(input('Qual o ano?'))
if n%4 == 0 and n%100 != 0:
    print('O ano é bissexto')
elif n%4 == 0 and n%400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
