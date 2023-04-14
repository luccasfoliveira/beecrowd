n = int(input())
texto = input().split()
if texto[1] == '+':
    print('OK' if int(texto[0]) + int(texto[2]) <= n else 'OVERFLOW')
else:
    print('OK' if int(texto[0]) * int(texto[2]) <= n else 'OVERFLOW')
