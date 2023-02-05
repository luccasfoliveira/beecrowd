L1 = list(map(int, input().split()))
maior = L1[0]
for i in L1[1:]:
    if i > maior:
        maior = i
print(maior)
