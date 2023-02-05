a, b = str(input('')).split()
a, b = int(a), int(b)

if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif a < b:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif b > a:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif b < a:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
