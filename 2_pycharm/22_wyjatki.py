def dzielenie1(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Wystapil blad')
        raise


def dzielenie2(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Wystapil blad dzielenia')
        raise
    except SyntaxError:
        print('Wystapil blad skladni')
        raise
    else:
        print('wynik wynosi',result)
    finally:
        print('proces zakonczony')


print(dzielenie2(15, 0))






