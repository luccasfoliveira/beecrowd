n = int(input())
for i in range(n):
    p = int(input())
    perfeito = False
    soma = 0
    for j in range(1, p):
        if p % j == 0:
            soma += j
            if soma == p:
                perfeito = True
                print(f'{p} eh perfeito')
                break
    if not perfeito:
        print(f'{p} nao eh perfeito')
