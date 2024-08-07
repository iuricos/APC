aux = input()
for i in aux:

    if i == "zero":
        uai = aux.replace("zero", "0")

    if "um" in aux:
        uai = aux.replace("um", "1")

    if "dois" in aux:
        uai = aux.replace("dois", "2")

    if "três" in aux:
        uai = aux.replace("três", "3")

    if "quatro" in aux:
        uai = aux.replace("quatro", "4")

    if "cinco" in aux:
        uai = aux.replace("cinco", "5")

    if "seis" in aux:
        uai = aux.replace("seis", "6")

    if "sete" in aux:
        uai = aux.replace("sete", "7")

    if "oito" in aux:
        uai = aux.replace("oito", "8")

    if "nove" in aux:
        uai = aux.replace("nove", "9")
    


print(uai)