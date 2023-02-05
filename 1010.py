codigo_peca1, numero_peca1, valor_unitario1 = input().split()
codigo_peca1, numero_peca1, valor_unitario1 = int(codigo_peca1), int(numero_peca1), float(valor_unitario1)

codigo_peca2, numero_peca2, valor_unitario2 = input().split()
codigo_peca2, numero_peca2, valor_unitario2 = int(codigo_peca2), int(numero_peca2), float(valor_unitario2)

valor_pago = (numero_peca1 * valor_unitario1) + (numero_peca2 * valor_unitario2)
print(f'VALOR A PAGAR: R$ {valor_pago:.2f}')
