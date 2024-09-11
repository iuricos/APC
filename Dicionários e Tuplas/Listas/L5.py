n = int(input())
corredores = {}

def list2dict(l):
    dicionario = {}
    for elemento in range(0, len(l), 2):
        dicionario[l[elemento]] = l[elemento+1]
    return dicionario 

for i in range(n):
    coisas = list(input().split())
    corredores[i+1] = list2dict(coisas)

interesse = int(input())    
if interesse <= n:
    media = sum(list(map(float, corredores[interesse].values())))/ len(corredores[interesse].keys())
    print(f'No corredor {interesse} encontramos:')
    print(', '.join(corredores[interesse].keys()))
    print(f'E o preço médio é {media:.2f}.')
else:
    print('Esse corredor não existe no mercado.')