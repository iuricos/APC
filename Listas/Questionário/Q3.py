N, M, f = map(int, input().split())
A = []

linha = 0
coluna = 0

maior = -1000000

linhas_res = []
res = []

for i in range(N):
    inputs = input().split()
    A.append(inputs)

#a matriz B (kernel) deve possuir dimensão n/f por m/f
def pegakernel(matriz, dim_k, posi_k, posj_k):
    kernel = []

    for i in range(posi_k, posi_k + dim_k):
        aux = matriz[i][posj_k:posj_k+dim_k]
        kernel.append(aux)
    
    return kernel

#navega entre os kerneis, de i e i+f e por consequencia de j até j+f armazenando os valores em uma matriz

while True:
    linhas_res = []
    while coluna < M:
        maior = -100000
        for i in pegakernel(A, f, linha, coluna):
            for k in i:
                k = int(k)
                if k > maior:
                    maior = k
        
        linhas_res.append(maior)
        linha += f
        
        if linha >= N:
            coluna += f
            linha = 0
            res.append(linhas_res)
            break

    if coluna >= M:
        break

transposta = list(zip(*res))

for linha in transposta:
    print(" ".join(map(str, linha)))


