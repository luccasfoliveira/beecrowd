soma = count = 0
while True:
    idade = int(input())
    if idade < 0: break
    count += 1
    soma += idade
print(f'{soma/count:.2f}')
