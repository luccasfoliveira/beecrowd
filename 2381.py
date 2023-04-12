n = input().split()

p = int(n[1]) - 1
n = [0] * int(n[0])

for i in range(len(n)):
    n[i] = input()
n.sort()
print(n[p])
