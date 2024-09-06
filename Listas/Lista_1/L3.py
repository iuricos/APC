vogais = [
    'a', 'á', 'à', 'ã', 'â', 'A', 'Á', 'À', 'Ã', 'Â',
    'e', 'é', 'è', 'ê', 'E', 'É', 'È', 'Ê',
    'i', 'í', 'ì', 'î', 'I', 'Í', 'Ì', 'Î',
    'o', 'ó', 'ò', 'õ', 'ô', 'O', 'Ó', 'Ò', 'Õ', 'Ô',
    'u', 'ú', 'ù', 'û', 'U', 'Ú', 'Ù', 'Û'
]

def paridade(palavra):
    cont = 0
    for letra in palavra:
        if letra in vogais:
            cont += 1
    if cont%2==0:
        return True
    else:
        return False


def paron(lista):
    pares = []
    for palavra in lista:
        if paridade(palavra):
            pares.append(palavra)
    return pares
