while True:
    try:
        n = int(input())
        espaco = n//2
        for i in range(1, n+1, 2):
            print(' ' * espaco + '*' * i)
            espaco -= 1
        espaco = n//2
        print('*'.rjust(espaco+1))
        print('***'.rjust(espaco+2))
        print()
    except EOFError:
        break
