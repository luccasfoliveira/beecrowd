n = int(input())
for i in range(1, n+1):
    for j in range(1, 4):
        print(f'{i**j}', end=' ' if j != 3 else '')
    print()
