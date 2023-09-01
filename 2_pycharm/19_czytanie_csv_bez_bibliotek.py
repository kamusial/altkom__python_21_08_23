#1. Odczyt pliku csv z zapisem poszczegolnych pol pliku csv z zapisem poszczegolnych pol
path = 'C:\\Users\\Student\\Desktop\\dzien2_projekt_pycharm\\rozliczenie.csv'
mode = 'r'
with open(path, mode) as pracownicy:
    content = pracownicy.readlines()

print(type(content))
print(len(content))
print(content)
print(content[0])

for i in range(len(content)):
    content[i] = content[i].split(',')   #podział linii po przecinku
print('Koniec czesci 1\n')

#2. Obliczenie sredniej wyplaty
total = 0
for i in range(1, len(content)):
    total += int(content[i][1])
print(f'srednia wyplata {round(total/(len(content)-1),2)}')

#3. Obliczenie liczby kobiet na macierzynskim
total = 0
for i in range(1, len(content)):
    content[i][4] = content[i][4].replace('\n', '')
    if content[i][4] == 't' and content[i][3] == 'k':
        total += 1
print(f'Liczba koniec na macierzynskiem = {total}')

path = 'C:\\Users\\Student\\Desktop\\dzien2_projekt_pycharm\\rozliczenie2.csv'
with open(path, 'a') as pracownicy2:
    content = pracownicy2.write('Nowe\n')