v = int(input())
p = int(input())

divisivel = v // p
resto = v % p

for i in range(p):
    if i < resto:
        print(divisivel + 1)
    else:
        print(divisivel)
