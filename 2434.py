n, s = input().split()
n, s = int(n), int(s)
menor = s
for i in range(n):
    valor = int(input())
    s = s + valor
    if s < menor:
        menor = s
print(menor)
