x, soma= 1, 0
while x <= 2:
    while True:
        n = float(input())
        if 0 <= n <= 10:
            soma += n
            break
        print('nota invalida')
    x += 1
print('media =', f'{soma/2:.2f}')
