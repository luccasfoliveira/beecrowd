a, b, c = str(input('')).split()
a, b, c = float(a), float(b), float(c)

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b > c:
    b, c = c, b

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if a ** 2 == b ** 2 + c ** 2:
        print('TRIANGULO RETANGULO')
    elif a ** 2 > b ** 2 + c ** 2:
        print('TRIANGULO OBTUSANGULO')
    elif a ** 2 < b ** 2 + c ** 2:
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c and c == a:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or c == a:
        print('TRIANGULO ISOSCELES')
