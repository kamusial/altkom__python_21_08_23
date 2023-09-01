# program pyta o liczbe członków rodziny i kasę
# i zwraca dochód na osobe (z uwzględnieniem 500+ )
# napiszmy funkcję, która to policzy

def dochod_na_osobe(liczba_osob, dochod_calkowity):
    # liczba_dzieci = liczba_osob - 2
    # dodatkowa_kasa = 500 * liczba_dzieci
    # dochod_na_os = (dochod_calkowity + dodatkowa_kasa) / liczba_osob
    # return dochod_na_os
    return ((liczba_osob - 2) * 500 + dochod_calkowity) / liczba_osob


kasa = int(input('Ile zarabiacie? '))
ile_osob = int(input('Ile was jest '))
print('Dochod na osobe wynosi', dochod_na_osobe(ile_osob, kasa))
