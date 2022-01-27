n = 0
c = 1
while c < 10 :
    n = int(input('Digite o número que você deseja ver a tabuada:'))
    if n < 0:
        print('O programa encerrou')
        break
    else:
        print(f'{n} x {1} = {n*1}')
        print(f'{n} x {2} = {n*2}')
        print(f'{n} x {3} = {n*3}')
        print(f'{n} x {4} = {n*4}')
        print(f'{n} x {5} = {n*5}')
        print(f'{n} x {6} = {n*6}')
        print(f'{n} x {7} = {n*7}')
        print(f'{n} x {8} = {n*8}')
        print(f'{n} x {9} = {n*9}')
    c += 1

