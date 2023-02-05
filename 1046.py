a, b = str(input('')).split()
a, b = int(a), int(b)

hora = 24

if a > b:
    hora = 24 - (a - b)
    print(f'O JOGO DUROU {hora} HORA(S)')
elif a < b:
    hora = ((24 - a) + b) - 24
    print(f'O JOGO DUROU {hora} HORA(S)')
else:
    print(f'O JOGO DUROU {hora} HORA(S)')
