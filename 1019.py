numero = int(input(''))

horas = numero // 60 ** 2
numero = numero - horas * 60 ** 2
minutos = numero // 60
numero = numero - minutos * 60
segundos = numero

print(f'{horas}:{minutos}:{segundos}')
