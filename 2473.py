escolha = list(map(int, input().split()))
msena = list(map(int, input().split()))
count = 0
for i in escolha:
    for j in msena:
        if i == j:
            count += 1
if count == 3:
    print('terno')
elif count == 4:
    print('quadra')
elif count == 5:
    print('quina')
elif count == 6:
    print('sena')
else:
    print('azar')
