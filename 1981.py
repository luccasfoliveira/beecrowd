from math import factorial

while True:
    # tornando a str numa lista
    palavra = input().split()
    if palavra[0] == '0': break
    # ordenando as letras
    palavra = sorted(palavra[0])

    # indice para prosseguir com a proxima letra,
    # diferente da anterior
    indice, dividendo = 0, 1
    for i in range(len(palavra)):
        # definindo a letra para comparação; e
        # count para reaizar as contagens das letras repetidas
        letra, count = palavra[indice], 1
        for j in range(indice + 1, len(palavra)):
            if letra == palavra[j]:
                count += 1
            else:
                # se a letra pesquisada não existir
                # mudo para a próxima letra, antecipando
                indice = j
                break
        if count != 1:
            # incrementando as repetições das letras
            # para realizar a divisão da fórmula
            dividendo *= factorial(count)
        # após verificada as opções, interrompo o laço
        # se a letra for igual à última letra da plavra
        if letra == palavra[len(palavra) - 1]: break
    print(f'{factorial(len(palavra)) // dividendo % 100000007}' if dividendo > 0 else f'{factorial(len(palavra))}')
