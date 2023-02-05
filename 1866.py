c = int(input())
for i in range(c):
    n = int(input())
    soma = 0
    for j in range(n):
        if j % 2 == 0:
            soma += 1
        else:
            soma -= 1
    print(soma)
