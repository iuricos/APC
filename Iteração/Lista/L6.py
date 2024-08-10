def fibonacci(n):
    a1 = 1
    a2 = 0
    a  = 1

    if n == 1:
        print("0")
    elif n == 2:
        print(f'0 ', end='')
    else:
        print(f'0 1 ', end='')
        for i in range(n-2):
            a = a1 + a2
            a1, a2 = a, a1
            print(f'{a}', end=" ")

    
