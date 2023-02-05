from random import randint

n = int(input())
A = [0]*n
for i in range(n):
    A[i] = [0]*3
    maior = 0
    for j in range(3):
        A[i][j] = randint(0, 100)
        if A[i][j] > maior:
            maior = A[i][j]
    print(*A[i])
