# program prosi o wprowadzenie danych
# i zapisuje nowych uzytkownikow
# uzytkownik decyduje, kiedy zakonczyc dzialanie

baza_osob = []

while True:
    lista_pomocnicza = []
    imie = input('Podaj imie: ')
    lista_pomocnicza.append(imie)
    nazwisko = input('Podaj nazwisko: ')
    lista_pomocnicza.append(nazwisko)
    wiek = int(input('podaj wiek: '))
    lista_pomocnicza.append(wiek)
    baza_osob.append(lista_pomocnicza)
    decision = input('Czy chcesz kontynuowac?: t/n  ')
    if decision.lower() != 't' and decision.lower() != 'tak':
        break

print(baza_osob)



