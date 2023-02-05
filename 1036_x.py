import math

A,B,C = map(float,input().split())

delta = math.pow(B,2) - (4.0 * A * C)

if delta < 0 or A ==0:
    print("Impossivel calcular")
else:
    r1 = (-B + delta ** (1 / 2)) / (2 * A)
    r2 = (-B - delta ** (1 / 2)) / (2 * A)
    print("R1 = %.5f" % (r1))
    print("R2 = %.5f" % (r2))
