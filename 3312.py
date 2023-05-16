def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**.5)+1):
        if numero % i == 0:
            return False
    return True


def fatorial(numero):
    for i in range(2, numero):
        numero *= i
    return numero


n = input()
n = list(map(int, input().split()))
for i in n:
    if primo(i):
        print(f'{i}! = {fatorial(i)}')
