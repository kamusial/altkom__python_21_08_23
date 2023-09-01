# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# sprawdźmy, ile osób chorowało w ostatnim roku na krzykach
print('Chorzy w ostatnim roku na krzykach', krzyki & chorzy_rok)
print('ilość: ',len(krzyki & chorzy_rok))
print('Chorzy w ostatnim roku na krzykach', chorzy_rok.intersection(krzyki))
print('ilość: ',len(chorzy_rok.intersection(krzyki)))

# sprawdźmy ile osób z Krzyków chorowało w ostatnim roku - taki sam wynik
# print('Chorzy w ostatnim roku na krzykach', chorzy_rok & krzyki)
# print('\nChorzy w ostatnim roku na krzykach ',krzyki.intersection(chorzy_rok))

# sprawdźmy, ile osób mieszka w sumie w centrum i na krzykach
print('W centrum i na krzykach mieszka w sumie', len(centrum | krzyki), 'osób')
print ('Ilość ',len(centrum.union(krzyki)))

# sprawdźmy poprawność danych:
# każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku
print('\nLiczba chorujący w ostatnim roku', len(chorzy_rok))
print('Liczba chorujący w ostatnim miesiącu', len(chorzy_miesiac))
print('Liczba chorujących w ostatnim roku i NIEchorujacyh w ostatnim miesiącu'\
,len(chorzy_rok - chorzy_miesiac))  #ok
print('Liczba chorujących w ostatnim miesiącu i NIEchorujacyh w ostatnim roku'\
,len(chorzy_miesiac - chorzy_rok))   #nok
#chorzy_miesiac.difference(chorzy_rok)

# nikt nie powinien mieszkać jendocześnie w centrum i na krzykach – jeśli tak, trzeba usunąć
print('Chorzy w ostatnim roku na krzykach', krzyki & chorzy_rok)
if len(krzyki & centrum) != 0:
    x = input('Usuwam. Usunąć ludzi z Krzyków (K), czy z Centrum (C) ?   ')
    if x.lower() == 'k':
        krzyki = krzyki - (krzyki & centrum)
#        krzyki = krzyki.difference(krzyki.intersection(centrum))
        print('Sprawdzam: ' ,len(krzyki & centrum))
    elif x.lower() == 'c':
        duplikaty = krzyki.intersection(centrum)
        for i in duplikaty:
            centrum.remove(i)
        print('Sprawdzam: ', len(krzyki.intersection(centrum)))
    else:
        print('nie udalo sie usunąć')

# każdy: chory, zdrowy, z krzyków i z centrum, powinien być w bazie NFZ.
# Jeśli nie ma, trzeba dopisać
poza_NFZ = (centrum.union(krzyki.union(chorzy_miesiac.union(chorzy_rok)))).difference(NFZ)
print(f'\nLudzie poza NFZ {poza_NFZ}, liczba tych osób {len(poza_NFZ)}\ndodaje do bazy NFZ')
NFZ = NFZ.union(poza_NFZ)
if len((centrum.union(krzyki.union(chorzy_miesiac.union(chorzy_rok)))).difference(NFZ)) == 0:
    print('ok')
else:
    print('Ups, nie udało się dodać do bazy. Wciąż mamy ',len(centrum.union(krzyki.union(chorzy_miesiac.union(chorzy_rok)))),' ludzi poza bazą NFZ')

# pesele żeńskie mają ostatnią cyfrę parzystą, męskie – nieparzystą.
# zróbmy nowe zbiory, osobne dla mężczyzn i kobiet (w NFZ)

print('\nDzielę zbiór NFZ na panów i panie')
NFZ_men = set()
NFZ_women = set()
for i in NFZ:
    if i % 2 == 0:
        NFZ_women.add(i)
    else:
        NFZ_men.add(i)
print('Sprawdzam\nPanie to ',NFZ_women,' \na Panowie to ',NFZ_men)