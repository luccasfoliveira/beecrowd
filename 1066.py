n1 = int(input(''))
n2 = int(input(''))
n3 = int(input(''))
n4 = int(input(''))
n5 = int(input(''))

par = 0
impar = 0
positivo = 0
negativo = 0

for i in (n1, n2, n3, n4, n5):
    if i % 2 == 0:
        par += 1
    if i % 2 != 0:
        impar += 1
    if i > 0:
        positivo += 1
    if i < 0:
        negativo += 1
        
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
