qnt = int(input())
for i in range(qnt):
    n = int(input())
    primo = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break
    if primo:
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')
