n = int(input())
t = int(input())
matriz = []

for i in range(n):
    matriz += [list(map(int, input().split()))]

def recursive_order(matriz, indice):
    if len(matriz) <= 1:
        return matriz

    pivo = matriz[0]
    menores = []
    maiores = []

    for i in range(1, len(matriz)):
        if matriz[i][indice] < pivo[indice]:
            menores.append(matriz[i])
        elif matriz[i][indice] > pivo[indice]:
            maiores.append(matriz[i])
        else:  
            if sum(matriz[i]) < sum(pivo):
                menores.append(matriz[i])
            else:
                maiores.append(matriz[i])

    return recursive_order(menores, indice) + [pivo] + recursive_order(maiores, indice)

ordenada = (recursive_order(matriz, t))

for i in ordenada:
    print(*i)