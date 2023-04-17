while True:
    try:
        d, n = input().split()
        d, n = int(d), int(n)
        soma = 0
        while n != 0:
            soma += n % 10
            n //= 10
        if soma % 3 == 0:
            print(soma, 'sim')
        else:
            print(soma, 'nao')
    except EOFError:
        break
