#dana list liczba 12345
#program oblicza i zwraca sumę cyfr

liczba = 12345
liczba_str = str(liczba)
suma = 0

for cyfra in liczba_str:
    suma += int(cyfra)
print(suma)
