while True:
    num = int(input())
    if num == -1:
        break
    valores = map(int, input().split())
    count = soma = 0
    for i in valores:
        soma += i
        if soma % 100 == 0:
            count += 1
    print(count)
