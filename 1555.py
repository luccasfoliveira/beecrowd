n = int(input())
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    r = ((3*x)**2) + (y**2)
    b = (2*x**2) + ((5*y)**2)
    c = (-100*x) + (y**3)

    if r > b and r > c:
        print('Rafael ganhou')
    elif b > c and b > r:
        print('Beto ganhou')
    else:
        print('Carlos ganhou')
