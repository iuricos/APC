emote = input()

while True:
    frase = input()
    frase = frase.replace(emote, '').replace(emote[::-1], '')

    print(frase)
    if frase == '':
        break