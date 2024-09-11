def JaChegou(n, s):
    if n == 1:
        print(s)
    else:
        n-=1
        print(s)
        JaChegou(n, s)
