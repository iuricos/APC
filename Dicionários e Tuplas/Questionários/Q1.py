def list2dict(l):
    d = {}
    for i in range(0 , len(l), 2):
        d[l[i]] = l[i+1]
    return d   

def reverse_lookup(d, val):
    for key in d:
        if d[key] == val:
            return key

dict_produtos = list2dict(input().split())
produtos_e_qnts = list2dict(input().split())
valor = 0

# bruma 2 Esmalte 3

for i in produtos_e_qnts:
    valor += (float(dict_produtos[i]) * float(produtos_e_qnts[i]))

print(f'R$ {valor:.2f}')