while True:
    try:
        a, b = input().split()
        a, b = int(a), int(b)
        print(abs(a-b))
    except EOFError:
        break
