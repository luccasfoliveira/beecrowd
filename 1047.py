a, b, c, d = str(input('')).split()
a, b, c, d = int(a), int(b), int(c), int(d)

h = c-a
if h < 0:
    h = (c+24)-a

m = d-b
if m < 0:
    m = (60+d)-b
    if h == 0:
        h = 23
    else:
        h -= 1

if a == b == c == d:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')
