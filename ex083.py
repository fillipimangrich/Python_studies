n = (input('Digite sua expressão:'))
lista = []
for i in n:
    if i == '(':
        lista.append(i)
    elif i == ')':
        if '(' in lista:
            lista.pop()
        else:
            lista.append(')')
            break
    
if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada')