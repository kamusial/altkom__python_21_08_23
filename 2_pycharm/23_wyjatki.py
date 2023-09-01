# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  zle dane, jeszcze raz")


while True:
    x = input("Wprowadz liczbe: ")
    try:
        x = int(x)
        print('Zrzutowane do int')
        break
    except ValueError:
        try:
            x = float(x)
            print('Zrzutowane do float')
            break
        except ValueError:
            print('Jeszcze raz')





print('dalsza czesc programu')