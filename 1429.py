from math import factorial

while True:
    n = int(input())
    if n == 0:
        break
    soma = 0
    for i in range(1, len(str(n))+1):
        soma += (n % 10) * factorial(i)
        n //= 10
    print(soma)
