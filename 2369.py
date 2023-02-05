n = int(input())
soma = 7
while True:
    if n <= 10: break
    if 11 <= n <= 30:
        soma += (n-10)
        break
    elif 31 <= n <= 100:
        soma += (n-30)*2
        n = 30
    elif n > 100:
        soma += (n-100)*5
        n = 100
print(soma)
