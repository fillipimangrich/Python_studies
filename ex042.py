n1 = int(input('Digite a reta 1: '))
n2 = int(input('Digite a reta 2: '))
n3 = int(input('Digite a reta 3: '))
if n1 + n2 <= n3 or n1 + n3 <= n2 or n2 +n3 <= n1:
    print('\033[1;32;40mNão da pra formar um triangulo\033[m')
elif n1 == n2 == n3:
    print('\033[1;32;40mo triângulo é equilatero\033[m')
elif n1 == n2 or n2 == n3 or n1 == n3:
    print('\033[1;32;40mNo triângulo é isóceles\033[m')
elif n1!=n2!=n3:
    print('\033[1;32;40mo triangulo é escaleno\033[m')

