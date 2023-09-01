def przywitanie(imie, wiek=15):
    if wiek < 18:
        print('Siema', imie)
    else:
        if imie[-1] == 'a':
            print('dzien dobry Pani')
        else:
            print('dzien dobry Panu')


przywitanie('Kamil')

