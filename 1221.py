n = int(input())
for i in range(n):
    primo = True
    num = int(input())
    if (num % 2 == 0 and num != 2) or num == 1:
        primo = False
    else:
        for i in range(3, int(num**.5)+1):
            if num % i == 0:
                primo = False

    print('Prime' if primo else 'Not Prime')
