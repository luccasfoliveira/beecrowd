while True:
    try:
        n = int(input())
        for i in range(n):
            T = float(input())
            if i == 0:
                menor = T
            if T < menor:
                menor = T
        print(menor)
    except EOFError:
        break
