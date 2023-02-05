# LER MEDIA DE ALUNO E CALCULAR O PESO E ESPECIFICAR SUAS CONDIÇÕES.

n1, n2, n3, n4 = str(input('')).split()
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)
media = ((2 * n1) + (3 * n2) + (4 * n3) + (1 * n4)) / (2 + 3 + 4 + 1)
if media >= 7.:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media >= 5. and media <= 6.9:
    exame = float(input(''))
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {exame}')
    media_final = (exame + media) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    print(f'Media final: {media_final:.1f}')
else:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
