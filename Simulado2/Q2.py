def sonho(n):
    x = abs(int(input()))
    print(n)
    if x%2 == 0:
        return
    else:
        n+=1
    sonho(n)
