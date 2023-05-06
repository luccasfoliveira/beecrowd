N = list(input().split())
L, Q = float(N[1]), float(N[2])
x, i = len(N)-1, 0
while L > Q:
    i %= len(N)-1
    L -= Q
print(f'{N[i]} {L:.2f}')
