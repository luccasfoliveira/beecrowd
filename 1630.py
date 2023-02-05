from math import gcd

while True:
    try:
        X, Y = input().split()
        X, Y = int(X), int(Y)
        if X == Y:
            print(4)
        else:
            FPB = gcd(X, Y)
            print((X // FPB) * 2 + (Y // FPB) * 2)
    except EOFError:
        break
