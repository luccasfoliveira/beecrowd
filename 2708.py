count = countQnt = 0
while True:
    saida = input().split()
    if saida[0] == 'ABEND':
        break
    elif saida[0] == 'SALIDA':
        count += 1
        countQnt += int(saida[1])
    else:
        count -= 1
        countQnt -= int(saida[1])
print(countQnt)
print(count)
