x = int(input())
lista = []

for i in range(x):
    lista.append(input())

impostores = input().split()

for i in range(len(lista)):
    for i in impostores:
        if i in lista:
            lista.remove(i)

print(*lista)