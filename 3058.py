n = int(input())
for i in range(n):
    a, b = input().split()
    c = float(a) * 1000 / int(b)

    if i == 0:
        menor = c
    elif c < menor:
        menor = c
print(f'{menor:.2f}')
