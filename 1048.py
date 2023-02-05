salario = float(input(''))

if salario <= 400.00:
    n_salario = ((salario * 15) / 100) + salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {n_salario - salario:.2f}')
    print('Em percentual: 15 %')
    
elif salario >= 400.01 and salario <= 800.00:
    n_salario = ((salario * 12) / 100) + salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {n_salario - salario:.2f}')
    print('Em percentual: 12 %')
    
elif salario >= 800.01 and salario <= 1200.00:
    n_salario = ((salario * 10) / 100) + salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {n_salario - salario:.2f}')
    print('Em percentual: 10 %')

elif salario >= 1200.01 and salario <= 2000.00:
    n_salario = ((salario * 7) / 100) + salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {n_salario - salario:.2f}')
    print('Em percentual: 7 %')

elif salario > 2000.00:
    n_salario = ((salario * 4) / 100) + salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {n_salario - salario:.2f}')
    print('Em percentual: 4 %')

