def list2dict(l):
    d = {}
    for i in range(0 , len(l), 2):
        d[l[i]] = l[i+1]
    return d   

n = int(input())
dict_produtos = {}

for i in range(n):
    preco = int()
    produtos = ''
    dados = input().split()
    for j in range(len(dados)):
        if j%2 ==0:
            produtos += dados[j] +", "
        else:
            preco += float(dados[j])
    dict_produtos[i+1] = produtos[:-2],preco/(len(dados)//2)
corredor =int(input())
if corredor not in dict_produtos.keys():
    print("Esse corredor não existe no mercado.")
else:
    print(f'No corredor {corredor} encontramos:\n{dict_produtos[corredor][0]}\nE o preço médio é {dict_produtos[corredor][1]:.2f}.')
            
    