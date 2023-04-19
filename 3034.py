def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
for i in range(n):
    n = int(input()) + 1
    if n % 7 == 0 and primo(n + 2):
        print('Yes')
    else:
        print('No')
