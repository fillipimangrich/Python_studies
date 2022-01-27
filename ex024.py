cidade = input('Qual sua cidade?')
cidade = cidade.upper()
cidade = cidade.split()

if cidade[0] == 'SANTO':
    print('A sua cidade começa com santo')
else:
    print('A sua cidade nao começa com santo')

