L = list(map(int, input().split()))

if L[0] < L[1]:
    L[0], L[1] = L[1], L[0]
if L[0] < L[2]:
    L[0], L[2] = L[2], L[0]
if L[1] < L[2]:
    L[1], L[2] = L[2], L[1]
print(L[1])
