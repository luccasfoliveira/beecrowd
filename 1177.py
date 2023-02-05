n = int(input())
L = []
x = 0
for i in range(1000):
    L.append(x)
    print(f'N[{i}] = {x}')
    x += 1
    if x == n:
        x = 0
