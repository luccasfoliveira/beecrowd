while True:
    L, R = input().split()
    if L == '0' and R == '0': break
    L, R = int(L), int(R)
    print(L+R)
