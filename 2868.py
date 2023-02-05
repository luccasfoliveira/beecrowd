n = int(input())
for i in range(n):
    L1 = input().split()
    L1[0], L1[2], L1[4] = int(L1[0]), int(L1[2]), int(L1[4])
    if '+' in L1 and L1[0] + L1[2] != L1[4]:
        diferenca = abs((L1[0] + L1[2]) - L1[4])
        print('E' + str('r'*diferenca) + 'ou!')

    elif 'x' in L1 and (L1[0] * L1[2]) != L1[4]:
        diferenca = abs((L1[0] * L1[2]) - L1[4])
        print('E' + str('r' * diferenca) + 'ou!')

    else: # 'x' in L1 and (L1[0] - L1[2]) != L1[4]
        diferenca = abs((L1[0] - L1[2]) - L1[4])
        print('E' + str('r' * diferenca) + 'ou!')
