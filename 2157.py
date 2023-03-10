n = int(input())
for i in range(n):
    texto = ''
    a, b = input().split()
    for j in range(int(a), int(b)+1):
        texto += str(j)
    print(texto+texto[::-1])
