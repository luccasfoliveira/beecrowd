while True:
    x, y = input().split()
    x, y = int(x), int(y)
    if y == x: break
    print('Decrescente' if x > y else 'Crescente')
