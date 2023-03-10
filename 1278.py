teste = 0
while True:
    n = int(input())
    if n == 0:
        break
    maior = 0
    string = list()
    for i in range(n):
        string.append(' '.join(input().split()))

        if maior < len(string[i]):
            maior = len(string[i])
    if teste == 1:
        print()

    for i in string:
        print(i.rjust(maior))

    teste = 1
