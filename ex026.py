frase = input('Digite uma frase:').strip()
frase = frase.lower()
caracteres = frase.count('a')
posicao = frase.find('a') + 1
ultima = frase.rfind('a') + 1
print(f'Nessa frase exitem {caracteres} "a" e aparece pela primeira vez na posição: {posicao} e pela ultima: {ultima}.')
