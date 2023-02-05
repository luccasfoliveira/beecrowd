x = int(input())
soma, count = x, 1
while True:
    z = int(input())
    if z > x: break
while z >= soma:
    x += 1
    count += 1
    soma += x
print(count)
