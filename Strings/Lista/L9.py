def não_possui_a_letra_u(palavra):
    for letra in palavra:
        if letra == 'u' or letra == 'ú' or letra == 'ù' or letra == 'ũ' or letra =='û' or letra == 'U' or letra == 'Ú' or letra == 'Ù' or letra == 'Ũ' or letra == 'Û':
            return False
    return True

print(não_possui_a_letra_u('Latex'))