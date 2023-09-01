# for i in range(2, 22, 3):
#     print(i)

x = range(2, 14, 3)
print(list(x))

mytuple = tuple(range(0, 101, 2))
print(mytuple)

#rozpakowywanie
data = (7, 'lipiec', 2004, 'wtorek')
#dzien = data[0]
dzien, miesiac, rok, dzien_tygodnia = data