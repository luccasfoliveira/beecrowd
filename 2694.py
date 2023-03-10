n = int(input())
for i in range(n):
    texto = input()
    soma = 0
    caracter = ''
    for i in texto:
        if i.isdigit():
            caracter += i
        elif caracter.isdigit():
            soma += int(caracter)
            caracter = ''
    else:
        if caracter.isdigit():
            soma += int(caracter)
    print(soma)
