def sonho(n):
    x = int(input())
    n+=1
    print(n)
    if x%2 == 0:
        return
    else:
        sonho(n)

sonho(1)