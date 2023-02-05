par, impar = [], []
for i in range(15):
    num = int(input())
    par.append(num) if num % 2 == 0 else impar.append(num)
    if len(par) == 5:
        for i in range(len(par)):
            print(f'par[{i}] = {par[i]}')
        par = []
    if len(impar) == 5:
        for i in range(len(impar)):
            print(f'impar[{i}] = {impar[i]}')
        impar = []

for i in range(len(impar)):
    print(f'impar[{i}] = {impar[i]}')
for i in range(len(par)):
    print(f'par[{i}] = {par[i]}')
