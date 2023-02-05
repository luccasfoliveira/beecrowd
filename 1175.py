L = []
for i in range(20):
    L.append(int(input()))
for i in range(10):
    L[i], L[len(L)-1-i] = L[len(L)-1-i], L[i]
for i in range(20):
    print(f'N[{i}] =', L[i])
