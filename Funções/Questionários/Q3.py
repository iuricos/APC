def print_rectangle(tam):
    print(tam)
    print('+'*tam)
    print('+'+' '*(tam - 2)+'+')
    print('+'*tam)

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

print_rectangle(a)
print_rectangle(b)
print_rectangle(c)
