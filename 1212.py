while True:
    n1, n2 = input().split()
    if n1 == '0' and n2 == '0':
        break
    n1, n2 = int(n1), int(n2)
    count, mais_1, = 0, 0
    while n1 != 0 or n2 != 0:
        if n1 >= 10 or n2 >= 10:
            soma = (n1 % 10) + (n2 % 10) + mais_1
            n1 = n1 // 10
            n2 = n2 // 10
            mais_1 = 0
            if soma > 9:
                count += 1
                mais_1 = 1
        else:
            soma = n1 + n2 + mais_1
            if soma > 9:
                count += 1
            n1 = n2 = 0

    if count == 0:
        print('No carry operation.')
    elif count == 1:
        print(f'{count} carry operation.')
    else:
        print(f'{count} carry operations.')
