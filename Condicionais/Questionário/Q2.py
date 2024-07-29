#ESTE CÓDIGO POSSUI ALGUM DETALHE INCORRETO

a = input(f"O programa funciona?\n")

if a == 'SIM':
    a = input("Você entende o que fez?\n")
    if a == 'SIM':
       print("Ótimo. Então não mexe!")
    if a == 'NÃO':
        a = input("Já foi na tutoria?\n")
        if a == 'SIM':
            print(f'Choremos!')
        if a == 'NÃO':
            print("Temos um time a disposição!")
else:
    a = input("Você sabe onde está o erro?\n")
    if a == 'SIM':
        a = input("Acha que pode solucionar sozinho?\n")
        if a == 'SIM':
            print("Então mão na massa!\n")
        if a == 'NÃO':
            a = input("Já pesquisou no Google?\n")
            if a == 'NÃO':
                a = input("Corre lá então!\n")
            if a == 'SIM':
                a = input("Já foi na tutoria?\n")
                if a == 'SIM':
                    print(f'Choremos!\n')
                if a == 'NÃO':
                    print("Temos um time a disposição!\n")
    if a == 'NÃO':
        a = input("Já foi na tutoria?\n")
        if a == 'SIM':
            print(f'Choremos!\n')
        if a == 'NÃO':
            print("Temos um time a disposição!\n")
    #ESTE CÓDIGO POSSUI ALGUM DETALHE INCORRETO
