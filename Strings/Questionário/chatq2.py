s = input()

if len(s) < 6 or len(s) > 32:
    print("Senha invalida.")
else:
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_caractere_invalido = False

    for char in s:
        if char.isdigit():
            tem_numero = True
        elif char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif not char.isalnum():
            tem_caractere_invalido = True
            break

    if tem_maiuscula and tem_minuscula and tem_numero and not tem_caractere_invalido:
        print("Senha valida.")
    else:
        print("Senha invalida.")
