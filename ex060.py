n = int(input('Digite um número:'))
c = n-1
#for c in range (n-1,1,-1):
#    n = n*c
#print(n)
while c > 0:
    n = n*(c)
    c -= 1
print (n)