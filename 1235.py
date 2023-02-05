n = int(input())
for i in range(n):
    frase = input()
    pri_metade = frase[:len(frase)//2]
    seg_metade = frase[len(frase)//2::]
    print(''.join(pri_metade[::-1] + seg_metade[::-1]))
