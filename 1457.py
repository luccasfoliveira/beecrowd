n = int(input())
for i in range(n):
    num = input()
    exc = abs(len(num) - len(num.replace("!", "")))
    fatorial = num = int(num.replace("!", ""))
    k = 1
    while num * (num - (k * exc)) >= 1:
        fatorial *= (num - (k * exc))
        k += 1
    print(fatorial)
