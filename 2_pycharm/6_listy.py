lista1 = [1, 2, 3, 'mama', 5.4, 'tata', 4, 5, 6, [7, 8, 9, 'tata']]

print(lista1[2:8:2])
print(lista1[:2:-2])   #od końca, do elementu z indexem 2, co drugi

lista1.append('nowy element')
print(lista1)   #duża lista
print(lista1[9])   #mała lista
print(lista1[9][3])    #słowo tata
print(lista1[9][3][2])     #literka 't'
print(lista1[9][3][2:].upper())    #kawałek stringa, duże litery



