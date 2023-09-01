def funkcja_jakas(a, b):
    return a+b, a-b, a*b    #można zwrócić kilka wartści


moja_krotka = (4, 5, 6, 7, 'mama', 'piesek')
print(moja_krotka)
print(type(moja_krotka))

print(funkcja_jakas(4, 7))
print(funkcja_jakas(4, 7)[1])

informacje = funkcja_jakas(6, -23)
print(informacje)
print(informacje[:2])
informacje = list(informacje)
print(informacje)
informacje.append(5)
informacje = tuple(informacje)
print(informacje)