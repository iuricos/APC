w = input()
cpos = 0
cwal = 0
sim = True

while True:
    p = input()

    if p != w and sim:
        cpos += 1
    else:
        sim = False

    if p == w:
        cwal += 1

    if p == '0':
        break

if cwal == 0:
    print('Wally sumiu...')
elif cwal == 1:
    print(f'Wally é a {cpos+1}a pessoa!')
elif cwal > 1:
    print(f'Wally tem {cwal-1} clone(s)!!!')
