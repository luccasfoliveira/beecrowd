a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
a //= 2
b //= 3
c //= 5

if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)
