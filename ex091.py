from random import randint
from operator import itemgetter
jogo = {}
ranking = []
for i in range(0, 4):
    jogo[f'Jogador {i+1}'] = randint(1, 6)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for k,i in enumerate(ranking):
    print(f'{k+1}° lugar: {i[0]}, tirou o número:{i[1]}')
