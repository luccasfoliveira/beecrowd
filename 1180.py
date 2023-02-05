N = int(input())
lista = list(map(int, input().split()))
menor = lista[0]
for i in range (len(lista)):
    if menor > lista[i]:
        menor = lista[i]
        index = i
print('Menor valor:', menor)
print('Posicao:', index)
