kolory_napojow = {
    'kawa': 'brazowy', 'herbata': 'zielony', 'cola': 'czarny', 'icetea': 'zielony'
}

print(type(kolory_napojow))
print(kolory_napojow)
print(kolory_napojow.keys())
print(kolory_napojow.values())
print(kolory_napojow.items())   #lista złożona z krotek

print(kolory_napojow['kawa'])   #wypisz wartość
print('Kawa ma kolor', kolory_napojow['kawa'])

for produkt in kolory_napojow.keys():
    print(produkt, ' : ',kolory_napojow[produkt])

napoj = input('Co chcesz pic?   ')
print(napoj,'ma kolor', kolory_napojow[napoj].upper())

kolory_napojow['woda'] = 'przezroczysta'   # dodanie element
print(kolory_napojow)
kolory_napojow['woda'] = 'brak'   #updatować wartość
print(kolory_napojow)
del kolory_napojow['woda']    #usunąć klucz i wartość
print(kolory_napojow)
#kolory_napojow.clear()    #wyczyścić słownik
print(kolory_napojow)

lista = ['mama', 'tata', 'pies', 'kot']
slowo1 = 'Kot'
slowo2 = 'kAwa'

if slowo1 in lista:
    print('slowo',slowo1,'znajduje sie w liscie')

if slowo2 in kolory_napojow:
    print('slowo',slowo2,'znajduje sie w slowniku')