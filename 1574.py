n = int(input())
for i in range(n):
    n = int(input())
    count = 0
    LISTA = [0]
    for j in range(1, n+1):
        inst = input().split()
        if inst[len(inst)-1] == 'LEFT':
            LISTA.append(-1)
        elif inst[len(inst)-1] == 'RIGHT':
            LISTA.append(1)
        else:
            LISTA.append(LISTA[int(inst[len(inst)-1])])
        count += LISTA[j]
    print(count)
