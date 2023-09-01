sum = 0
ilosc = int(input('Podaj liczbe:    ' ))

for i in range (ilosc+1):
    print('i wynosi',i)
    print('petla kreci sie ',i+1,'-ty raz\n')
    if (i%2 == 0):
        sum += i
print(sum)
print('\n')






