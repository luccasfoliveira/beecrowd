x, y = input().split()
x, y = int(x), int(y)
a = 1
while a != y:
    for i in range(x):
        print(a, end='' if a % x == 0 else ' ')
        if a == y: break
        a += 1
    print()
