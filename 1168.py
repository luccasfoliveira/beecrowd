numDeLeds = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
n = int(input())
for i in range(n):
    soma = 0
    qnt = input()
    for i in range(len(qnt)):
        indice = int(qnt)%10
        soma += numDeLeds[indice-1]
        qnt = int(qnt)//10
    print(soma, 'leds')
