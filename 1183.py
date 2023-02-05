resp = input().upper()
mat = []
soma = count = 0
for i in range(12):
    mat.append([])
    for j in range(12):
        mat[i].append(float(input()))
for i in range(12):
    for j in range(i+1, 12):
        soma += mat[i][j]
        count += 1

if resp == 'M':
    media = soma / count
    print(f'{media:.1f}')
else:
    print(f'{soma}')
