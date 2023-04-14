while True:
    n = int(input())
    if n == 0:
        break
    n = list(map(int, input().split()))
    seg, x = 10, 0
    for i in n[1:]:
        if i >= n[x] + 10:
            seg += 10
        else:
            seg += i - n[x]
        x += 1
    print(seg)
