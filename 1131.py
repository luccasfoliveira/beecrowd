count_i = count_g = e = 0
while True:
    i, g = input().split()
    i, g = int(i), int(g)
    if i > g:
        count_i += 1
    elif i < g:
        count_g += 1
    else:
        e += 1
    r = int(input('Novo grenal (1-sim 2-nao)\n'))
    if r == 2: break

print(count_g + count_i + e, 'grenais')
print(f'Inter:{count_i}\n'
      f'Gremio:{count_g}\n'
      f'Empates:{e}')

if count_g > count_i:
    print('Gremio venceu mais')
elif count_i == count_g:
    print('Nao houve vencedor')
else:
    print('Inter venceu mais')
