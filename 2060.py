n = int(input())
texto = input().split()
countDois = countTres = countQuatro = countCinco = 0
for i in range(n):
    if int(texto[i]) % 2 == 0:
        countDois += 1
    if int(texto[i]) % 3 == 0:
        countTres += 1
    if int(texto[i]) % 4 == 0:
        countQuatro += 1
    if int(texto[i]) % 5 == 0:
        countCinco += 1

print(f"{countDois} Multiplo(s) de 2")
print(f"{countTres} Multiplo(s) de 3")
print(f"{countQuatro} Multiplo(s) de 4")
print(f"{countCinco} Multiplo(s) de 5")
