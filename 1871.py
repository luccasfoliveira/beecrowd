while True:
    m, n = input().split()
    if m == n == '0':
        break

    print(str(int(m) + int(n)).replace('0', ''))
