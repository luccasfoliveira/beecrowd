'''n = int(input())
x = [0]*n
for i in range(n):
    x[i] = [1]*n
    for j in range(1, n-1):
        x[i+1][j] = 2
    print(*x[i])
'''
from random import randint

mat = []
for i in range(5):
    mat.append([])
    for j in range(5):
        mat[i].append(randint(1,40))
        print(f'{mat[i][j]:02}', end=' ')
    print()
