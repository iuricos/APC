emote = input()
emote_inv = emote[::-1]

while True:
    frase= input()
    if frase == '':
        break
    else:
        frase = frase.replace(emote, '').replace(emote_inv, '')
        print(frase)