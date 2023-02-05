n = int(input())
soma = 0
for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    if b < a:
        soma += b
print(soma)
