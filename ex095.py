jogador = {
    'nome': list(),
    'partidas': list(),
    'gols':list(),
    'golpartida':list()
}
golpartida = list()
k = 0
while True:
    nome = input('Digite o nome do jogador: ')
    jogador['nome'].append(nome)
    partidas = int(input('Digite quantos jogos esse jogador jogou: '))
    jogador['partidas'].append(partidas)
    gol = 0
    for i in range(0,partidas):
        n = int(input(f'Quantos jogos ele marcou no jogo {i+1}: '))
        golpartida.append(n)
        gol += n
    jogador['golpartida'].append(golpartida[::])   
    jogador['gols'].append(gol)
    golpartida.clear()
    continuar = input('Deseja continuar? s/n ').lower()
    if continuar == 'n':
        break
print('='*40)
print(f'{"n":<3}', end='')
print(f"{'nome':<10}", end='')
print(f"{'gols por partida':<25}", end='')
print(f"{'gols totais':<12}")
for k in range(0,len(jogador['nome'])):
    print(f'{k+1:<3}', end='')
    print(f"{jogador['nome'][k]:<10} ", end='' )
    print(f"{str(jogador['golpartida'][k]):<25} ", end='' )
    print(f"{jogador['gols'][k]:<3}",)
print('='*40)
while True:
    busca = int(input('Quer mostrar os dados de qual jogador?')) - 1
    
    if busca == 998:
        break
    elif busca >= (len(jogador['nome'])):
        print('Error, esse jogador não existe!')
    else:
        print(f"O jogador {jogador['nome'][busca]} fez {jogador['gols'][busca]} em {jogador['partidas'][busca]} jogos ")
print(f'{"FIM":^30}')