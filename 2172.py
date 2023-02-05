while True:
    x, m = input().split()
    if x == '0' and m == '0':
        break
    x, m = int(x), int(m)
    print(x*m)
