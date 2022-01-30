from random import randint

numeros = (randint(0,100), randint(0,100), randint(0,1000), randint(0,1000), randint(0,1000))
print(numeros)
print(f'o maior valor é {max(numeros)}')
print(f'o menor valor é {min(numeros)}')