x = 1
while True:
    n = int(input())
    if n == 0: break
    ing = input().split()
    print('Teste', x)
    for i in range(len(ing)):
        ing[i] = int(ing[i])
        if i+1 == ing[i]:
            print(i+1 if i+1 == ing[i] else '\n')
            print()
    x += 1
