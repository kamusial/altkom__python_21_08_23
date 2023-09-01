baza_osob = [
    ['Kamil', 'Musial', 35],
    ['Beata', 'K', 21]
]

print(baza_osob[1])
print(baza_osob[1][2])

nowy_user = ['Piotr', 'P', 35]

baza_osob.append(nowy_user)    #dorzuca na koniec listy jako JEDEN element
#baza_osob.extend(nowy_user)    #dorzuca na koniec listy jako osobne elementy

print(baza_osob)

