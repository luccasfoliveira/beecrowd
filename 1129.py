LETRAS = ["A", "B", "C", "D", "E"]
while True:
    n = int(input())
    if n == 0:
        break
    for j in range(n):
        notas = list(map(int, input().split()))
        count = 0
        for i in notas:
            if i <= 127:
                count += 1
                if count > 1:
                    break
                letra = i

        if count == 1:
            print(LETRAS[notas.index(letra)])
        else:
            print('*')