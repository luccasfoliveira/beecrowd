a, b, c, d = str(input('')).split()
a, b, c, d = int(a), int(b), int(c), int(d)

if (b > c) and (d > a) and (c + d) > (a + b) and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
