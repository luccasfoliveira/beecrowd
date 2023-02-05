alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
for i in range(n):
    texto = input()
    nova_palavra = str()

    for c in texto:
        if c in alfabeto:
            nova_palavra += chr(ord(c) + 3)
        else:
            nova_palavra += c

    nova_palavra = list(nova_palavra[::-1])

    index = len(nova_palavra) // 2
    for i in nova_palavra[len(nova_palavra) // 2::]:
        nova_palavra[index] = chr(ord(i) - 1)
        index += 1

    print(''.join(nova_palavra))
