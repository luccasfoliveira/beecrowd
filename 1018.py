valor = int(input(''))

valor_atual = valor

nota_100 = valor_atual // 100
valor_atual = valor_atual % 100

nota_50 = valor_atual // 50
valor_atual = valor_atual % 50

nota_20 = valor_atual // 20
valor_atual = valor_atual % 20

nota_10 = valor_atual // 10
valor_atual = valor_atual % 10

nota_5 = valor_atual // 5
valor_atual = valor_atual % 5

nota_2 = valor_atual // 2
valor_atual = valor_atual % 2

nota_1 = valor_atual // 1
valor_atual = valor_atual % 1

print(valor)
print(f'{nota_100} nota(s) de R$ 100,00')
print(f'{nota_50} nota(s) de R$ 50,00')
print(f'{nota_20} nota(s) de R$ 20,00')
print(f'{nota_10} nota(s) de R$ 10,00')
print(f'{nota_5} nota(s) de R$ 5,00')
print(f'{nota_2} nota(s) de R$ 2,00')
print(f'{nota_1} nota(s) de R$ 1,00')
