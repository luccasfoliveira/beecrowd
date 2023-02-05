x = int(input())
a = 1
for i in range(x):
    for j in range(1, 5):
        if j % 4 == 0:
            print('PUM')
        else:
            print(a, end=' ')
        a += 1
