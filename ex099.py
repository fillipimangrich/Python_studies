def maior(*numeros):
    print(f'foram informados {len(numeros)} valores, são eles: {numeros}')
    print(f'o maior valor é: {max(numeros)}')
maior(5,1,45,20,154)
maior(1,4,54)
maior(5,20,-3)
maior(-2,0)