x = 1
while True:
    dinheiro = int(input())
    if dinheiro == 0: break
    nota= 50
    print('Teste', x)
    x += 1
    while nota != 0:
        count = dinheiro//nota
        dinheiro %= nota
        print(count, end=' ' if nota != 1 else '\n\n')
        if nota == 1:
            nota = 0
            break
        if nota == 50:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
