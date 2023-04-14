n = int(input())
n = list(map(int, input().split()))
count = 0
for i in range(len(n)):
    if n[i] == 1:
        count += 1
print(count)
