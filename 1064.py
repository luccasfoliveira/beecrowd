n1 = float(input(''))
n2 = float(input(''))
n3 = float(input(''))
n4 = float(input(''))
n5 = float(input(''))
n6 = float(input(''))

count = 0
soma = 0

for i in (n1, n2, n3, n4, n5, n6):
    if i > 0:
        count += 1
        soma += i
media = soma / count
print(f'{count} valores positivos\n{media:.1f}')
