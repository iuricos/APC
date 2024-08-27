mediav = 0
count = 0

while True:
    n, v = input().split(',')
    
    if n == 'Fim':
        break

    v = float(v)
    mediav += v
    count += 1
        
print(f'{mediav/count:.2f}')
print(f'{count:-^10}')