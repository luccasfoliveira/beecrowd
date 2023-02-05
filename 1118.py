while True:
    while True:
        n1 = float(input())
        if n1 < 0 or n1 > 10:
            print('nota invalida')
        else:
            break

    while True:
        n2 = float(input())
        if n2 < 0 or n2 > 10:
            print('nota invalida')
        else:
            break

    media = (n1 + n2) / 2
    print(f'media = {media:.2f}')

    resp = 0
    while True:
        if resp < 1 or resp > 2:
            resp = int(input('novo calculo (1-sim 2-nao)\n'))
        else:
            break
    if resp == 2:
        break
