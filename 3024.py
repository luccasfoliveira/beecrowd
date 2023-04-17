n = input().split()
metros = int(n[1])
n = list(map(int, input().split()))
x = count = 0
for i in n[1:]:
    if i - n[x] <= 2:
        count += 1
    x += 1
print(count)
