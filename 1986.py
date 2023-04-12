def baseNumero(numero):
    B = "0123456789ABCDEF"
    conversor = 0
    x = len(numero) - 1
    for i in numero:
        conversor += 16 ** x * B.index(i)
        x -= 1
    return conversor


n = int(input())
n = input().split()
for i in range(len(n)):
    n[i] = chr(baseNumero(n[i]))
print(''.join(n))
