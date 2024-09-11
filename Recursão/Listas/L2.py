bomba = int(input())
recorde = int(input())
if recorde < bomba:
    explodir = True
else:
    explodir = False

def bombaa(tempo , explodir):
    if tempo == 0:
            print('Cabum!!!! Explodiu')
            return ''
    if recorde < bomba:
        if tempo == 5:
            print('Seu tempo está acabando!')
            bombaa(tempo-1, explodir)
        elif tempo == 1:
            print('Seja rápido. Falta 1 segundo')
            print('Cabum!!!! Explodiu')
        else:
            print(f'Atenção faltam {tempo} segundos...')
            bombaa(tempo-1, explodir)
    else:
        if tempo == 5:
            print('Seu tempo está acabando!')
            bombaa(tempo-1, explodir)
        elif tempo == 1:
            print('Bomba desativada automaticamente!')
        else:
            print(f'Atenção faltam {tempo} segundos...')
            bombaa(tempo-1, explodir)

        


bombaa(bomba, recorde)