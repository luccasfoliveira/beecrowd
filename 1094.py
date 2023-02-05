N = int(input())
soma_c = soma_r = soma_s = 0
for i in range(N):
    quantia, tipo = input().upper().split()
    quantia = int(quantia)
    if tipo == 'C':
        soma_c += quantia
    elif tipo == 'R':
        soma_r += quantia
    else:
        soma_s += quantia
total = soma_c + soma_s + soma_r
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {soma_c}')
print(f'Total de ratos: {soma_r}')
print(f'Total de sapos: {soma_s}')
print(f'Percentual de coelhos: {soma_c/total*100:.2f} %')
print(f'Percentual de ratos: {soma_r/total*100:.2f} %')
print(f'Percentual de sapos: {soma_s/total*100:.2f} %')
