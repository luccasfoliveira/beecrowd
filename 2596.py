num = int(input())
for i in range(num):
    impar = 1
    n = int(input())
    for j in range(2, n+1):
        if j * j <= n:
            impar += 1
        else:
            break
    print(n - impar)
