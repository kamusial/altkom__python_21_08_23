lista = [5, 4, 'mama', 5.76, True, False, 4332]

#for i in range (50, 21, -7):   #(od=0, do, krok=1)
#    print(i)

print(lista[0])
print(type(lista[2]))
#print(lista[7])   #max index to 6

print(len(lista))    # dlugość listy
print(len(lista[2]))   #długosc stringa

for i in range (len(lista)):
    print(i+1,'element listy to',lista[i])

for element in lista:
    print(element)
