haslo = input('Podaj haslo ')
proby = 3

while haslo != '1234' and proby > 1:   #blad logiczny

    print('zle haslo')
    proby -= 1   #zmniejsz o jeden
    haslo = input('Podaj haslo ')

print('gratulacje, masz dostep do systemu')

