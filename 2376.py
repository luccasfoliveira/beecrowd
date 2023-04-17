LISTA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
x = 0
while len(LISTA) != 1:
    m, n = input().split()
    m, n = int(m), int(n)

    if m > n:
        LISTA.pop(x + 1)
    else:
        LISTA.pop(x)
    x += 1
    if x == len(LISTA):
        x = 0

print(LISTA[0])
