n = int(input())
for i in range(n):
    A, B = input().split()
    A = int(A)
    print('encaixa' if A % 10**len(B) else 'nao encaixa')
