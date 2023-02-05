while True:
    try:
        n = int(input())
        x = [0]*n
        for i in range(n):
            x[i] = [3]*n
            x[i][i] = 1
            x[i][n-1-i] = 2
            for j in range(n):
                print(f'{x[i][j]}', end='')
            print()
    except EOFError:
        break
