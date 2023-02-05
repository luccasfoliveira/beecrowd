while True:
    soma = 0
    x, y = input().split()
    x, y = int(x), int(y)
    if y > x:
        x, y = y, x
    if x <= 0 or y <= 0:
        break
    for i in range(y, x+1):
        soma += i
        print(i, end=' ')
    print(f'Sum={soma}')
