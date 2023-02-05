n = []
n.append(int(input()))
for i in range(1, 10):
    n.append(n[i-1] * 2)
for i in range(10):
    print(f'N[{i}] = {n[i]}')
