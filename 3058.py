n = int(input())
for i in range(n):
    a, b = input().split()
    a, b = float(a), int(b)

    if i == 0:
        menor = a * 1000 / b
    elif a * 1000 / b < menor:
        menor = a * 1000 / b
print(f'{menor:.2f}')
