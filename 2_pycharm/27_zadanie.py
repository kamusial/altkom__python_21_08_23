#program czyta plik tekstowy
#za pomocą funkcji, sprawdza ile jest unikalnych słów i ile razy dane słowo sie powtarza
#za pomoca funkcji, sprawdz liczbe pustych linii
def laczenie_stringow(lista_stringow: list):
    nowy_string = ''
    for string in lista_stringow:
        nowy_string += string
    return nowy_string


def unikalke_slowa(dane: str):
    nowe_dane = dane.split()
    return len(set(nowe_dane))


def powtorzenia(dane: str):
    slownik_powtorzen = {}
    lista_slow = dane.split()
    for slowo in lista_slow:
        if slowo in slownik_powtorzen:
            slownik_powtorzen[slowo] += 1
        else:
            slownik_powtorzen[slowo] = 1
    return slownik_powtorzen



def czyszczenie_danych(string):
    return string.lower().replace('(','').replace(')','').replace('.','').replace(',','')


with open('rollingstones.txt', 'r') as file:
    content = file.readlines()

content = laczenie_stringow(content)
content = czyszczenie_danych(content)
print('powtorzenia ',powtorzenia(content))
print('liczba unikalnych slow', unikalke_slowa(content))




