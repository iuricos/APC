m, n = list(map(int, input().split()))
sala = []
distancia = []
distancia_de_um_zero = []

for i in range(m):
    fileira = list(map(int, input().split()))
    sala.append(fileira)

for fileira in sala:
    for index in range(len(fileira)):
        linha_dir = []
        linha_esq = []
        distancia_de_um_zero = []
        if fileira[index] == 0:
            if 1 in fileira[index:] and 0 in fileira[index:]:
                linha_dir = fileira[index:]
            if 1 in fileira[:index+1] and 0 in fileira[:index+1]:
                linha_esq = fileira[:index+1]
                linha_esq = linha_esq[::-1]
            
            if linha_dir:
                distancia_dir = abs(linha_dir.index(1))
            else:
                distancia_dir = 999
            if linha_esq:
                distancia_esq = abs(linha_esq.index(1))    
            else:
                distancia_esq = 999

            distancia_de_um_zero.append(distancia_esq)
            distancia_de_um_zero.append(distancia_dir)
            print(distancia_de_um_zero)
        distancia.append(distancia_de_um_zero)

print(distancia)

caralho = []

for i in distancia:
    if i:
        caralho.append(min(i))

print(max(caralho))