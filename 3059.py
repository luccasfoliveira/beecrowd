n, i, f = input().split()
n, i, f = 0, int(i), int(f)
numeros = list(map(int, input().split()))
for j in range(len(numeros)):
    for k in range(j, len(numeros)):
        if numeros[j] == numeros[k]:
            continue
        if i <= (numeros[j] + numeros[k]) <= f:
            n += 1
print(n)
