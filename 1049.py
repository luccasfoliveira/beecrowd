animal_1 = str(input('')).strip().upper()
animal_2 = str(input('')).strip().upper()
animal_3 = str(input('')).strip().upper()

if animal_1 == 'VERTEBRADO':
    if animal_2 == 'AVE':
        if animal_3 == 'CARNIVORO':
            print('aguia')
        elif animal_3 == 'ONIVORO':
            print('pomba')

if animal_1 == 'VERTEBRADO':
    if animal_2 == 'MAMIFERO':
        if animal_3 == 'ONIVORO':
            print('homem')
        elif animal_3 == 'HERBIVORO':
            print('vaca')

if animal_1 == 'INVERTEBRADO':
    if animal_2 == 'INSETO':
        if animal_3 == 'HEMATOFAGO':
            print('pulga')
        elif animal_3 == 'HERBIVORO':
            print('lagarta')

if animal_1 == 'INVERTEBRADO':
    if animal_2 == 'ANELIDEO':
        if animal_3 == 'HEMATOFAGO':
            print('sanguessuga')
        elif animal_3 == 'ONIVORO':
            print('minhoca')
