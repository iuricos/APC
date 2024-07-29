x = int(input())
y = 0

while y <= x:
    if (y % 3 == 0) and (y % 7 == 0):
        print(f'{y}', end=" ")
    y +=1
