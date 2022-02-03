lista = []
dados = []
pesado = 1
leve = 10000
listapesado = []
listaleve = []
while True:
    dados.append(input('Digite o nome: '))
    dados.append(int(input('Digite o peso: ')))
    lista.append(dados[:])
   
    if dados[1] > pesado:
         listapesado.clear()
         pesado = dados[1]
         listapesado.append(dados[0])

    elif dados[1] == pesado:
         listapesado.append(dados[0])

    elif dados[1] < leve:
         listaleve.clear()
         leve = dados[1]
         listaleve.append(dados[0])

    elif dados[1] == leve:  
         listaleve.append(dados[0])

    dados.clear()
    n = input('Deseja continuar? s/n ').lower()
    if n == 'n':
        break
print(f'O total de pessoas cadastradas foram: {len(lista)}')
print(f'O maior peso foi {pesado}kg. Peso de {listapesado}')
print(f'O menor peso foi {leve}kg. Peso de {listaleve}')
