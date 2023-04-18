n = int(input())
for i in range(n):
    a, b = input().split()
    c = int(a) * int(b)
    if int(a) != int(b):
        count = 0
    else:
        count = 1

    while c - 9 >= 9:
        c -= 9
        count += 1
    if c != 9:
        count -= 1
    print(count)
