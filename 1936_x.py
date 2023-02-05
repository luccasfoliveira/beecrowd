from math import factorial

n = int(input())
soma = 0
x = 9
while soma != n:
    soma -= factorial(x)
    if soma > n:
        x -= 1
