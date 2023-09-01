def mnozenie_zaokraglone(a: [int, float, list], b: float):   #parametry danego typu
    return round((a * b), 5)


def lepsze_mnozenie_zaokraglone(*liczby):     # dowolna liczba argumentów
    wynik = 1
    for liczba in liczby:
        wynik *= liczba
    return round(wynik, 5)


def lepsze_mnozenie_zaokraglone2(liczby: tuple):     # taka sama funkcjonalność, jeden argument - krotka
    wynik = 1
    for liczba in liczby:
        wynik *= liczba
    return round(wynik, 5)


def wypisz(**dane):    # dowolna liczba keyword argumentów
    print(dane)
    if 'nazwisko' in dane:
        print(f'Dzien dobry Panie {dane["nazwisko"]}')


# def jakas_funkcja(a, b, *args, **kwargs):    # kolejność argumentów


wypisz(imie='Kamil', nazwisko='Musial', wiek=35)
print(mnozenie_zaokraglone(100, 1.1), 4, 434)



