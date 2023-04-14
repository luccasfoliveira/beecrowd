n = int(input())
count = maior = 0
for i in range(n):
    caminho = input()
    if i % 2 == 0:
        for i in caminho:
            if i == 'o':
                count += 1
                if count > maior:
                    maior = count
            elif i == 'A':
                count = 0
    else:
        for i in caminho[::-1]:
            if i == 'o':
                count += 1
                if count > maior:
                    maior = count
            elif i == 'A':
                count = 0
print(maior)
