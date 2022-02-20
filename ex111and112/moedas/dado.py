def verificar(n):
    n = n.replace(',','.').strip()
    if n.isalpha():
        n = input('Digite um valor válido:')
        verificar(n)
    else:
        float(n)

