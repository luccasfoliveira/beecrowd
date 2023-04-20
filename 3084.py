while True:
    try:
        a, b = input().split()
        a = int(a) // 30
        b = int(b) // 6

        print(f'{a:02}:{b:02}')

    except EOFError:
        break
