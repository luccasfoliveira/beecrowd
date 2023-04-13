while True:
    n = int(input())
    if n == 0:
        break
    for j in range(n):
        LETRAS = ["A", "B", "C", "D", "E"]
        notas = list(map(int, input().split()))
        for i in range(5):
            if notas[i] <= 127:
                notas[i] = True
                if notas.count(True) > 1:
                    break
            else:
                notas[i] = False

        if notas.count(True) == 1:
            print(LETRAS[notas.index(True)])
        else:
            print('*')
