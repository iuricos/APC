def controle(total, tomados):
    tomados += 1
    total -= 1
    if total == 0:
        print('Parabens Julie! Voce tomou todos os {total} comprimidos!')
    else:
        print(f'Voce ja tomou {tomados} comprimidos, restam {total}.')
        controle(total, tomados)