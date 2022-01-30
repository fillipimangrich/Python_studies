times=('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'Os cincos primeiros colocados são:{times[0:6]}')
print(f'Os últimos 4 colocados foram: {times[-4:]}')
print(f'Os times em ordem alfabética é: {sorted(times)}')
print(f'O chapecoense ficou na {times.index("Chapecoense")+1}° posição')