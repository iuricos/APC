# No mínimo uma letra maiuscula, uma letra minuscula e um caráter numérico

# Nenhum caractere de acentuação, pontuação ou espaço

# Entre 6 e 32 caracteres (inclusivo)


senha = input()
tamanho = False
maiuscula = False
minuscula = False
pontuacao = False

if 6<=len(senha)<=32:
    tamanho = True

for i in senha:
    if i.islower():
        minuscula = True
    if i.isupper():
        maiuscula = True

if i.isalnum():
    pontuacao = True

print(minuscula)
print(maiuscula)
print(tamanho)
print(pontuacao)

if minuscula and maiuscula and tamanho and pontuacao :
    print("senha valida")
else:
    print("senha invalida")

B3LBaXYM45Re8YXmP7WXu3RKTMU6rtDTVgqhkh8Ja
