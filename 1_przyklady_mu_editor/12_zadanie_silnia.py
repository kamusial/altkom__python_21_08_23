#oblicz silnie (petla while i for)

while True:
    ile = int(input('Silnia z ilu?   '))
    if ile >= 0:
        break

wynik = 1
for i in range (2, ile+1):
    wynik *= i
print('Wynik',wynik)

wynik = 1
while ile > 1:
    wynik *= ile
    ile -= 1
print('Wynik',wynik)


