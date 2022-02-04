dict = {
'nome':input('Digite o nome: '),
'media':int(input('Digite a média: ')),
'situação':''}
if dict['media']<7:
    dict['situação'] = 'reprovado'
else:
    dict['situação'] = 'Aprovado'
print(f'o nome é {dict["nome"]} ')
print(f'a média é {dict["media"]} ')
print(f'a situação é {dict["situação"]}')