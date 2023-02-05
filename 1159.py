while True:
    n = int(input())
    if n == 0: break
    soma = 0
    for i in range(n, n+10):
        if i % 2 == 0:
            soma += i
    print(soma)
