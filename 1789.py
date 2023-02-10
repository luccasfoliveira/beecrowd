while True:
    try:
        n = int(input())
        lista = map(int, input().split())
        count10 = count20 = count30 = 0
        for i in lista:
            if i < 10:
                count10 += 1
                if count20 > 0 and count30 > 0:
                    break
            elif i < 20:
                count20 += 1
            else:
                count30 += 1
                break

        if count30 > 0:
            print(3)
        elif count20 > 0:
            print(2)
        else:
            print(1)

    except EOFError:
        break
