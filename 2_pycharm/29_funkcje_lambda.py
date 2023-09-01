mnozenie = lambda a, b: a*b if (b > 0) else None

dodaj_vat = lambda x: x * 1.23

print(dodaj_vat(mnozenie(100, 1.1)))

#funkcja map

def podwoj(x):
    return 2*x


liczby = (1, 2, 3, 4)
nowe_liczby = [5, 6, 7, 8]

wynik = map(podwoj, liczby)   #mapowanie
print(list(wynik))

wynik = map(lambda x: 2 * x, liczby)   #mapowanie, z funkcją lambda
print(list(wynik))

wynik = map(lambda x, y: x + y, liczby, nowe_liczby)   #wiecej, niż jeden argument
print(list(wynik))


#list comprehension
sprzety = ['komputer', 'monitor', 'klawiatura']
nowe_sprzety = []

for x in sprzety:
    if 'a' in x:
        nowe_sprzety.append(x)
print(nowe_sprzety)

nowe_sprzety = []
nowe_sprzety = [x for x in sprzety if 'a' in x]
print(nowe_sprzety)

liczby1 = [1, 4, 43, 4343, 44]
liczby2 = [x * 2 for x in liczby1 if x % 2 == 0]
print(liczby2)
liczby2 = [x * 2 if x % 2 == 0 else 0 for x in liczby1]   #list comprehension z else
