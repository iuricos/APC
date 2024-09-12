N, M, f = map(int, input().split())
matriz = []

for i in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)

def pega_kernel(matriz, tam_kernel, pos_i, pos_j): # Dada determinada posição e tamanho, pego a submatriz de uma matriz maior.
    kernel = []
    for i in matriz[:tam_kernel+pos_j]:
        kernel.append(i[pos_i:tam_kernel+pos_i])
    return kernel

def maior_do_kernel(kernel): #desempacoto um kernel(submatriz) e pego o seu maior valor
    desempacotada = []
    for i in kernel:
        for num in i:
            desempacotada.append(num)
    maior_num = max(desempacotada)
    return maior_num 

def max_pooling(matriz): #Função que navega por uma determinada matriz, pegando os seus maiores valores!
    pos_i = 0
    pos_j = 0
    resultante = []

    for i in range(N//f): 
        temp = []
        pos_i = 0
        for j in range(M//f):
            temp.append(maior_do_kernel(pega_kernel(matriz, f, pos_i, pos_j)))
            pos_i += f
        resultante.append(temp)
        pos_j += f
    return resultante

for i in max_pooling(matriz): #Imprime o resultado da maneira que o exercício pediu
    print(*i)