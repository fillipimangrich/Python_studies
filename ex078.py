listanum = []
for c in range(0,5):
    listanum.append(int(input(f'Digite o valor {c+1}: ')))
print(listanum)

print(f'O maior valor da lista é {max(listanum)} e está na posição: ', end='')

for k, c in enumerate(listanum):
    if c == (max(listanum)):
        print(f'{k}, ', end='')
print()
print(f'O menor valor da lista é {min(listanum)} e está na posição: ', end='')

for k, c in enumerate(listanum):
    if c == (min(listanum)):
        print(f'{k}, ', end='')