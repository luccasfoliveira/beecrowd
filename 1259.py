n = int(input())
par, impar = [], []
for i in range(n):
    num = int(input())
    par.append(num) if num % 2 == 0 else impar.append(num)
par = sorted(par)
impar = sorted(impar, reverse=True)
for i in par:
    print(i)
for i in impar:
    print(i)
