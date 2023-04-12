def primo(numero):
    if (numero % 2 == 0 and numero != 2) or numero <= 1:
        return False

    for i in range(3, int(numero ** .5) + 1):
        if numero % i == 0:
            return False
    return True


def primoGemeos(numero):
    x = 1
    while True:
        if primo(numero-x) and primo(numero-x-1):
            return numero-x, numero-x-1
        if primo(numero+x) and primo(numero+x+1):
            return numero+x, numero+x+1
        x += 1
    
    
print(*primoGemeos(int(input())))
