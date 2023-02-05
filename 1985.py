n = int(input())
soma = 0
for i in range(n):
    p, q = input().split()
    p, q = int(p), int(q)
    if p == 1001:
        valor = 1.5
    elif p == 1002:
        valor = 2.5
    elif p == 1003:
        valor = 3.5
    elif p == 1004:
        valor = 4.5
    else:
        valor = 5.5
    soma += valor * q
print(f'{soma:.2f}')
