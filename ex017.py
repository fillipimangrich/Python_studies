from math import sqrt
cateto_oposto = float(input('Digite o cateto oposto:'))
cateto_adjacente = float(input('Digite o cateto adjacente:'))
hipotenusa = sqrt((cateto_oposto**2)+(cateto_adjacente**2))
print(f'O cateto oposto é {cateto_oposto} o adjacente {cateto_adjacente} e a hipotenusa vale {hipotenusa}')
