n = int(input())
for i in range(n):
    A, B = input().split()
    A, B = int(A), int(B)
    while (A >= B and A%10 == B%10) and B != 0:
        A //= 10
        B //= 10
    print('encaixa' if B == 0 else 'nao encaixa')
