A1 = int(input())
A2 = int(input())
A3 = int(input())
A1 = 2 * A2 + 4 * A3
A2 = 2 * A1 + 2 * A3
A3 = 2 * A2 + 4 * A1

if A1 <= A2 and A1 <= A3:
    posicionar = A1
elif A2 <= A1 and A2 <= A3:
    posicionar = A2
else:
    posicionar = A3
print(posicionar)
