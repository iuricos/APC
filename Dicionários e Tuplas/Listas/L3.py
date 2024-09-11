def list2dict(l):
    d = {}
    for i in range(0, len(l), 2):
        d[l[i]] = l[i+1]
    return d  

catalogo = list2dict(input().split())
desejados = list2dict(input().split())

soma = int()

for produto in desejados:
    soma += float(catalogo[produto]) * int(desejados[produto])
print(f'R$ {soma:.2f}')