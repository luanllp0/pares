lista =[]
pares =[]
for i in range (0, 5):
    x = int(input())
    lista.append(x)
for j in lista:
    if j % 2 == 0:
        pares.append(j)
print(pares)