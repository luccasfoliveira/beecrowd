n1 = input().split()
for i in range(len(n1)):
    n1[i] = int(n1[i])

sorteada = sorted(n1)
for i in sorteada:
    print(i)
print()
for i in n1:
    print(i)
