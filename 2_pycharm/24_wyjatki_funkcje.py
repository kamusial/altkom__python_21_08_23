def can_be_int(x):
    try:
        int(x)
        return True
    except:
        return False


def can_be_float(x):
    try:
        float(x)
        return True
    except:
        return False


x = input('Wprowadz liczbe ')
if can_be_int(x) or can_be_float(x):
    print(round(float(x) * 5))
else:
    print('zle dane')
