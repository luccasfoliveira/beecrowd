n = int(input())
S, N, TOTAL = [], [], []
for i in range(n):
    nome = input()
    S.append(nome[2:]) if "+" in nome else N.append(nome[2:])

TOTAL += S
TOTAL += N
TOTAL = sorted(TOTAL)
for i in TOTAL:
    print(i)
print(f'Se comportaram: {len(S)} | Nao se comportaram: {len(N)}')
