n = int(input())
for i in range(n):
    texto = input().upper()
    count = 0
    for c in texto:
        if c not in 'AEIOU':
            count += 1
            if count == 3:
                print(texto.capitalize(), "nao eh facil")
                break
        else:
            count = 0
    else:
        print(texto.capitalize(), "eh facil")
