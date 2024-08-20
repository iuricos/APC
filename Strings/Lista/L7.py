aux = input()
palindromo = False
contra = aux[::-1]
contadif = 0

i = 0


if aux == contra:
    palindromo = True

while True:
    c = aux[i]
    d = aux[-(i + 1)]
    if c != d:
        contadif += 1
    i += 1
    if i == len(aux):
        break

contadif = contadif/2

if contadif == 1:
    print('ON')
elif palindromo and (len(aux) % 2 != 0):
    print('ON')
else:
    print('OFF')

