while True:
    try:
        n = int(input())
        count = 0
        while n != 1:
            n //= 2
            count += 1
        print(count)
    except EOFError:
        break
