n = int(input())
L = list(map(int, input().split()))
for i, n in enumerate(L):
    if i+1 == 1:
        menor, indice = n, i+1
    if n < menor:
        menor, indice = n, i+1
print(indice)
