#Gra "zgadnij jaką liczbę mam na myśli"?
#użytkownik wprowadza liczbę z przedziału <1,100>
#Program pyta użytkownika o liczbę i mówi, czy podana liczba jest większa, mniejsza bądź równa wylosowanej.

liczba1 = 70

while True:
    liczba2 = int(input('Wprowadz liczbe: '))
    if liczba2 > liczba1:
        print('za duzo')
    elif liczba2 < liczba1:
        print('za malo')
    else:
        print('trafiłeś')
        break

print('dalsza czesc programu')
