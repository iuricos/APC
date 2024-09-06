linha, coluna = map(int, input().split())
grade = []
vetor = []
coord_bomba = []

for i in range(linha):
    grade.append([0] * coluna)

qnt = int(input())
for i in range(qnt):
    lugar = list(map(int, input().split()))
    coord_bomba.append(lugar)

def bombear_em_cruz(bomba, terreno):
    x = bomba[0]-1
    y = bomba[1]-1
    
    for m in range(linha):
        grade[m][y] += 1

    for n in range(coluna):
        grade[x][n] += 1
    grade[x][y] -= 1

    return terreno

for bomba in coord_bomba:
    bombear_em_cruz(bomba, grade)

maximo = int()
quantos = int()
for i in grade:
    if max(i) > maximo:
        maximo = max(i)

for i in grade:
    quantos += i.count(maximo)

print(quantos)