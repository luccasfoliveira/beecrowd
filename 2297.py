teste = 1
while True:
    n = int(input())
    if n == 0:
        break
    soma = 0
    for i in range(1, n + 1):
        a, b = input().split()
        a, b = int(a), int(b)

        soma += a - b

    print('Teste', teste)
    teste += 1
    if soma < 0:
        print('Beto\n')
    else:
        print('Aldo\n')
