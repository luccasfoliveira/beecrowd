maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
senha = ''
n = int(input())
for i in range(n):
    texto = input("")
    variacao = int(input())
    for j in texto:
        senha += maiusculo[(maiusculo.index(j) + variacao) % 26]

print(senha)
