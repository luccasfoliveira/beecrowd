n = int(input())
for i in range(n):
    monte = input()
    Q = False
    J = False
    K = False
    A = False
    for j in monte:
        if j == 'Q':
            Q = True
        elif j == 'J':
            J = True
        elif j == 'K':
            K = True
        elif j == 'A':
            A = True

    if Q and J and K and A:
        print("Aaah muleke")
    else:
        print("Ooo raca viu")
