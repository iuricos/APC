N, M, K = map(int, input().split())
q = list(map(int, input().split()))  

precos = []

for i in range(N):
    precos.append(list(map(int, input().split())))

comprados = []
menor_que_necessario = False
soma = int()

for i in precos:
    i = sorted(i)
    comprados.append(i[:K])
    if len(i) < K:
        menor_que_necessario = True


for i in comprados:
    soma += sum(i)


if soma > M or menor_que_necessario:
    print('Nao')
else:
    print('Sim')

