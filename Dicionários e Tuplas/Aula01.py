eng2sp = {'one': 'uno', 'two':'dos', 'three':'tres'}


# Desafio: Implementar inverte_dict usando set.default

def inverte_dict(d):
    inv = {}
    val = d[k]
    for k in d:
        if d[k] not in inv:
            inv[val] = d[k]
        else:
            inv[val].append(k)
    return inv

a = (2, 9, 10)
print(len(a))