maior, x = 0, 1
while x <= 100:
    num = int(input())
    if maior < num:
        maior = num
        index = x
    x += 1
print(maior)
print(index)
