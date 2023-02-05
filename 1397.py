while True:
    qnt = int(input())
    if qnt == 0: break
    c_a = c_b = 0
    for i in range(qnt):
        a, b = input().split()
        a, b = int(a), int(b)
        if a > b:
            c_a += 1
        elif b > a:
            c_b += 1
    print(c_a, c_b)
