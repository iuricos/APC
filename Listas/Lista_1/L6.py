def mediana_e_mais_proximo_media_e_pos(lista):
    copia_lista = lista[:]
    lista = sorted(lista)
    tam = len(lista)

    if tam > 0:
        if tam % 2 == 0:
            mediana = (lista[int(tam/2)] + lista[int(tam/2-1)])/2
        else:
            mediana = (lista[int(tam/2)])

        somador = sum(lista)
        media = somador/tam

        delta = lista[tam-1] - lista[0]
        prox_media = lista[0]
        index=0

        for i in range(len(copia_lista)):
            if abs(media-copia_lista[i]) < delta:
                prox_media = copia_lista[i]
                index = i
                delta = abs(media - copia_lista[i])

    else:
        prox_media = None
        mediana = None
        index = None
    return [mediana, prox_media, index]
