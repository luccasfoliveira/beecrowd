N = int(input())
t1 = 0
t2 = 1
cont = 3
if N >= 2:
    print(t1, t2, end="")
while cont <= N:
    t3 = t2 + t1
    print("", t3, end="")
    t1 = t2
    t2 = t3
    cont = cont + 1
if N == 1:
    print(t1, end="")
print("\n", end="")
