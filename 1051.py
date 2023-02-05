salario = float(input(''))

if salario <= 2000.00:
    print('Isento')
elif salario >= 2000.01 and salario <= 3000.00:
    imposto = (salario - 2000) * 0.08
    print(f'R$ {imposto:.2f}')
elif salario >= 3000.01 and salario <= 4500.00:
    reajuste = salario - 3000
    imposto_reajuste = reajuste * 0.18
    imposto_reajuste_2 = ((salario - reajuste) - 2000) * 0.08
    print(f'R$ {imposto_reajuste + imposto_reajuste_2:.2f}')
elif salario > 4500.00:
    reajuste = salario - 4500
    imposto_reajuste = reajuste * 0.28
    reajuste_1 = (salario - reajuste) - 3000
    imposto_reajuste_1 = reajuste_1 * 0.18
    imposto_reajuste_2 = (((salario - reajuste) - reajuste_1) - 2000) * 0.08
    print(f'R$ {imposto_reajuste + imposto_reajuste_1 + imposto_reajuste_2:.2f}')
