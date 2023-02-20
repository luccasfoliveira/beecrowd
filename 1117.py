x, soma= 0, 0
while True:
    n = float(input())
    if 0 <= n <= 10:
        soma += n
        x += 1
    else:
        print('nota invalida')

    if x == 2:
        break

print('media =', f'{soma/2:.2f}')
