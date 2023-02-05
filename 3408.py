n = int(input())
SOMA = 0
for i in range(n):
    valor = input()
    for letra in valor:
        if letra.isalpha():
            valor = valor.replace(letra, '')
    SOMA += int(valor)
print(SOMA)
