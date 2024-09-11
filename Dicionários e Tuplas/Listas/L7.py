def convert(lista):
    dicionario = {}
    for i in lista:
        if i[0] not in dicionario:
            dicionario[i[0]] = [i[1]]
        else:
            dicionario[i[0]].append(i[1])
    return dicionario