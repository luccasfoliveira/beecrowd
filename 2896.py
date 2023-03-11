n = int(input())
for i in range(n):
    texto = input().split()
    print(int(texto[0]) // int(texto[1]) + int(texto[0]) % int(texto[1]))
