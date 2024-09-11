def corrida(voltaspfinal, voltasfaltam, voltasuportadas):
    voltaspfinal -= 1
    voltasfaltam -= 1
    if voltaspfinal == 0:
        print('A corrida chegou ao fim.')
    else:
        if voltasfaltam == 0:
            print(f'Faltam {voltaspfinal} voltas, hora de trocar os pneus.')
            voltasfaltam = voltasuportadas
            corrida(voltaspfinal, voltasfaltam, voltasuportadas)            
        else:
            corrida(voltaspfinal, voltasfaltam, voltasuportadas)