n = input().split()
metros = int(n[1])
n = list(map(int, input().split()))
x = 0
count = 1
for i in n[1:]:
    if n[x] <= i + 2:
        count += 1
    x += 1
print(count)
