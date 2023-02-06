while True:
    n = int(input())
    if n == 0:
        break
    soma = 0
    for i in range(1, n+1):
        soma += i**2
    print(soma)
