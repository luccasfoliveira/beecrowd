n = int(input())
a, l, p = input().split()
a, l, p = int(a), int(l), int(p)
if a < n or l < n or p < n:
    print('N')
else:
    print('S')
