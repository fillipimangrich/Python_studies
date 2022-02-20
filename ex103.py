def ficha(nome = '<desconhecido>', gols=0):
    print(f'o jogador {nome} marcou {gols} gols no campeonato.')

n = input('digite o nome: ')
g = input('digite quantos gols ele marcou: ')
if n.strip() == '' and g.isnumeric():
    ficha(gols=g)
elif n.strip() == '':
    ficha()
elif g.strip() == '':
    ficha(nome = n)
else:
    ficha(n,g)