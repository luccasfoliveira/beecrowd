n = int(input())
count = 0
if n % 2 == 0:
    print(f'{n**2//2} casas brancas e {n**2//2} casas pretas')
else:
    for i in range(1, n*n+1):
        if i % 2 != 0:
            count += 1
    print(f'{count} casas brancas e {count-1} casas pretas')
