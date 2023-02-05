vezes = int(input(''))

soma_d = 0
soma_f = 0

for i in range(0, vezes):
    n = int(input(''))
    if n >= 10 and n <= 20:
        soma_d += 1
    else:
        soma_f += 1
print(f'{soma_d} in')
print(f'{soma_f} out')
