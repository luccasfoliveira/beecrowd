L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))
yes = L1[0] != L2[0]
for i in range(1, 5):
    if yes and L1[i] == L2[i]:
        yes = False
        break
print('Y' if yes else 'N')
