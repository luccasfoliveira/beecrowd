A = []
for i in range(4):
    A.append(int(input()))
    if A[i] <= 0:
        A[i] = 1
    print(f'X[{i}] = {A[i]}')
