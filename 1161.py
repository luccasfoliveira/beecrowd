from math import factorial

while True:
    try:
        m, n = input().split()
        soma = factorial(int(m)) + factorial(int(n))
        print(soma)
    except EOFError:
        break
