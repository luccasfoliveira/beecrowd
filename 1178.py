L = [float(input())]
for i in range(100):
    L.append(L[i]/2)
    print(f'N[{i}] = {L[i]:.4f}')
