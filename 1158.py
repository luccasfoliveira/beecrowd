n = int(input())
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    soma = 0
    while y > 0:
        if x % 2 == 0:
            x += 1
            soma += x
        else:
            soma += x
        x += 2
        y -= 1
    print(soma)
