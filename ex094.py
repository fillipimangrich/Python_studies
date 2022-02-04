lista = []
idadetotal = 0
listamulheres = []
listaacima = []
while True:
    pessoa = {
    'nome': input('Digite o nome: '),
    'sexo': input('Digite o sexo: m/f '),
    'idade': int(input('Digite a idade: '))
    }
    idadetotal += pessoa['idade']
    lista.append(pessoa)
    if pessoa['sexo'] == 'f':
        listamulheres.append(pessoa['nome'])
    continuar = input('Deseja continuar? s/n ').lower()
    if continuar == 'n':
        break
media = idadetotal/(len(lista))
for i in lista:
    if i['idade'] > media:
        listaacima.append(i['nome'])

print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média de idade foi: {media:2f}')
print(f'Todas as mulheres cadastradas foram: {listamulheres}')
print(f'Todas as pessoas com idade acima da média foram : {listaacima}')
