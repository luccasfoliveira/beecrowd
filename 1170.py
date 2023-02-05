n = int(input())
for i in range(n):
    kg = float(input())
    dias = 0
    while kg > 1:
        kg /= 2
        dias += 1
    print(dias, 'dias')
