n = int(input())
for j in range(n):
    i = soma = 1
    n = int(input())
    while i < n:
        soma += 2**i
        i += 1
    print(soma)
