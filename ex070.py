preco_menor = 0
preco = 0
mais_1000 = 0
nome_menor = 0
nome = 0
total = 0
while True:
    nome = input('Digite o nome:')
    preco = float(input('Digite o preço:'))
    total += preco
    if preco > 1000:
        mais_1000 += 1
    if preco <= preco_menor or preco_menor == 0:
        nome_menor = nome
        preco_menor = preco

    continuar = input('Quer continuar? [S] [N]').upper()
    if continuar == 'N':
        break
print(f'O total da compra foi {total}, {mais_1000} custaram mais de 1000 reais e o mais barato foi {nome_menor}')
