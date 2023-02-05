n = int(input())
soma = 0
for i in range(n):
    t, v = input().split()
    soma += int(t) * int(v)
print(soma)
