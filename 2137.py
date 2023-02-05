while True:
    try:
        n = int(input())
        L = []
        for i in range(n):
            L.append(int(input()))
        L = sorted(L)
        for i in L:
            print(f'{i:04}')
    except EOFError:
        break
