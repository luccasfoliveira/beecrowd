N = int(input())
for i in range(N):
    count = 0
    x, y = input().split()
    x, y = int(x), int(y)
    if x > y:
        x, y = y, x
    for i in range(x+1, y):
        if i % 2 == 1:
            count += i
    print(count)
