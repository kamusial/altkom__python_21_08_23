def funkcja_jakas(a, b):
    return a+b, a-b, a*b    #można zwrócić kilka wartści

print(funkcja_jakas(4, 7))
print(funkcja_jakas(4, 7)[1])

print('Mamy taki \awyraz')
print('Mamy taki \bwyraz')
print('Mamy taki \fwyraz')
print('Mamy taki \nwyraz')
print('Mamy taki \rwyraz')
print('Mamy taki \twyraz')
print('Mamy taki \vwyraz')

slowo = 'kawa'
#slowo = slowo.upper()
nowe_slowo = slowo[:2] + 'A' + slowo[2:]
print(nowe_slowo)

print('abnormal', 'a\bnormal')

print(chr(260))    #zamieć na znak
print(ord('s'))    #zamień na unicode
print('\u0104')    #hex na znak - ważne 4 znaki


#print_format
a = b = c = 5
mama, tata = 'Maria', 'Zbigiew'
print('Mama nazywa sie',mama,', a tata',tata)
print(f'Mama nazywa sie {mama}, a tata {tata}')
print('Mama nazywa sie {}, a tata {}'.format(mama, tata))




