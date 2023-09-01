slowo1 = 'Amsterdam'
slowo2 = 'Berlin'

print(slowo1[2:5])
print(slowo1[4:-2])
print(slowo1[4:])
print(slowo1[:5])

print(slowo1[::-2]) #od końca, co drugi znak

print(slowo1 + slowo2)
print(slowo1[:3] + '-' + slowo2[:3])

print('mama'.replace('m', 'M', 1))

mail = 'kamil.support@gmail.com'
print(mail.find('@'))  #szukanie
print(mail.rfind('.'))  #szukanie od końca
print(mail[mail.find('@')+1:mail.rfind('.')])
print('mama'.upper())


