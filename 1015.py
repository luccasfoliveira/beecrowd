import math
x1, y1 = input().split()
x2, y2 = input().split()
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
formula = (x2 - x1)**2 + (y2-y1)**2
distancia = math.sqrt(formula)
print('{0:.4f}'.format(distancia))
