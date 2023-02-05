n = int(input())
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    print('divisao impossivel' if y == 0 else f'{x/y}')
