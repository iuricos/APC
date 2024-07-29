def drone(x):
    x = str(x)
    for digit in reversed(x):
        if digit == '1':
            print("Norte")
        elif digit == '2':
            print("Sul")
        elif digit == '3':
            print("Leste")
        elif digit == '4':
            print("Oeste")
    print("Trajeto Completo!")