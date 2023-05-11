num = list(map(int, input().split()))
A = num[0]
i = 1
while num[i] <= 0:
    i += 1
N = num[i]
soma = A
for i in range(1, N):
    soma += A + i
print(soma)
