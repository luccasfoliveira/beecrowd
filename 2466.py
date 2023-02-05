n = int(input())
L1 = list(map(int, input().split()))
while len(L1) != 1:
    index = 0
    for i in range(1, len(L1)):
        if L1[i] == L1[index]:
            L1.insert(index, 1)
            L1.pop(i)
        else:
            L1.insert(index, -1)
            L1.pop(i)
        index += 1
        if i == len(L1)-1: L1.pop()
print('branca' if L1[0] == -1 else 'preta')
