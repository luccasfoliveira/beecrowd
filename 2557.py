while True:
    try:
        texto = input()
        if texto[0].isdigit() and texto[2].isdigit():
            print(int(texto[0]) + int(texto[2]))

        elif not texto[0].isdigit() and texto[2].isdigit():
            print(int(texto[4]) - int(texto[2]))

        elif texto[0].isdigit() and not texto[2].isdigit():
            print(int(texto[0]) - int(texto[4]))
    except EOFError:
        break
