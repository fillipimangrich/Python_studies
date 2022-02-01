palavras = ('batata','arroz','feijao','carne','cerveja','agua','prato')
vogais = ('a','e','i','o','u')
for n in palavras:
    print(f'A palavra {n} tem as seguintes vogais: ', end='')
    for i in n:
        if i in vogais:
            print(i, end=' ')
    print('')