x, y ,z = map(int, input().split())
tipo = input()

if tipo == 'P':
    p1, p2, p3 = map(int, input().split())
    v = ((x * p1) + (y * p2) + (z*p3))/(p1+p2+p3)
    print(f'Ponderada\n{v:.2f}')
elif tipo == 'H':
    v = 3 / (1/x + 1/y + 1/z)
    print(f'Harmonica\n{v:.2f}')
elif tipo == 'A':
    v = (x + y + z) / 3
    print(f'Aritmetica\n{v:.2f}')
else:
    print(f'Operacao inexistente')