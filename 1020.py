numero = int(input(''))

anos = numero // 365
numero = numero - anos * 365
meses = numero // 30
numero = numero - meses * 30
dias = numero

print(f'{anos:.0f} ano(s)\n'
      f'{meses:.0f} mes(es)\n'
      f'{dias:.0f} dia(s)')
