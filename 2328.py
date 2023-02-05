num = int(input())
L = list(map(int, input().split()))
soma = L[0]-1
for i in range(1, len(L)):
    soma += L[i]-1
print(soma)
