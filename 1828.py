n = int(input())
for i in range(1, n+1):
    resp = input().split()
    if resp[0] == resp[1]:
        print(f'Caso #{i}: De novo!')
    elif (resp[0] == 'lagarto' or resp[0] == 'tesoura') and resp[1] == 'pedra':
        print(f'Caso #{i}: Raj trapaceou!')
    elif (resp[0] == 'pedra' or resp[0] == 'Spock') and resp[1] == 'papel':
        print(f'Caso #{i}: Raj trapaceou!')
    elif (resp[0] == 'papel' or resp[0] == 'lagarto') and resp[1] == 'tesoura':
        print(f'Caso #{i}: Raj trapaceou!')
    elif (resp[0] == 'Spock' or resp[0] == 'papel') and resp[1] == 'lagarto':
        print(f'Caso #{i}: Raj trapaceou!')
    elif (resp[0] == 'tesoura' or resp[0] == 'pedra') and resp[1] == 'Spock':
        print(f'Caso #{i}: Raj trapaceou!')
    else:
        print(f'Caso #{i}: Bazinga!')
