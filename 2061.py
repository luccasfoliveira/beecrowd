x, y = input().split()
x = int(x)
for i in range(int(y)):
    y = input()
    if y == 'fechou':
        x += 1
    else:
        x -= 1
print(x)
