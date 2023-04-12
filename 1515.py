while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        texto = input().split()
        if i == 0:
            menor = int(texto[1]) - int(texto[2])
            planeta = texto[0]
        if menor > int(texto[1]) - int(texto[2]):
            menor = int(texto[1]) - int(texto[2])
            planeta = texto[0]
    print(planeta)
