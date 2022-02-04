jogador = {
    'nome': input('Digite o nome do jogador: '),
    'partidas': int(input('Digite a quantidade de partidas: '))
}
jogador['gols'] = 0
lista = list()
for i in range(0,jogador['partidas']):
    n = int(input(f'Digite a quantidades de gol da partida {i+1}: '))  
    lista.append(n)
    jogador['gols'] +=  n
jogador['golpartida'] = lista
print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas")
for i,k in enumerate(lista):
    print(f'na partida {i+1} marcou {k}')
print(f"o total foi de {jogador['gols']}" )