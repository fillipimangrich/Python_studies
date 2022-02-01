lista = ('lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120,
         'Caneta', 2.5,
         'Livro', 32.6)
for i in lista:
    if type(i)==str:
          print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>6.2f}')