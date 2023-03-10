n = int(input())
for i in range(n):
    a, b = input().split('k')
    a = a[-3:0:-1]
    b = b[:-2]
    print('k' + a * b.count("a"))
