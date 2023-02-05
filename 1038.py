n, n1 = input('').split()
n, n1 = int(n), int(n1)
if n == 1:
    n = 4.0
    print(f'Total: R$ {n * n1:.2f}')
elif n == 2:
    n = 4.50
    print(f'Total: R$ {n * n1:.2f}')
elif n == 3:
    n = 5.
    print(f'Total: R$ {n * n1:.2f}')
elif n == 4:
    n = 2.
    print(f'Total: R$ {n * n1:.2f}')
elif n == 5:
    n = 1.5
    print(f'Total: R$ {n * n1:.2f}')
