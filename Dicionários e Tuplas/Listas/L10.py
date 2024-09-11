def stockmarket(lista):
    d = {}
    for i in lista:
        if i[0] not in d:
            d[i[0]] = float(i[1]*i[2])
        else:
            d[i[0]] += float(i[1]*i[2])
    return d
