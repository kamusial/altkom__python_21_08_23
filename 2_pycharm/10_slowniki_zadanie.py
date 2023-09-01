# stworzyć program, który pozwoli:
#dodać użytkownika
#sprawdzić, czy proponowane haslo jest dozwolone
#potwierdzic proponowane haslo
#zmiane hasla
#usunac uzytkownika
#usunac wszystkich uzytkownikow - to moze tylko KamilM

def is_password_allowed(passwd):
    if passwd not in hasla_niedozwolone:
        print('haslo dozwolone')
        return True
    else:
        print('haslo niedozwolone')
        return False

def logging():
    the_user = input('Wpisz nazwe uzytkownika:  ')
    the_password = input('Wpisz haslo:  ')
    if the_user in users and the_password == users[the_user]:
        print('logowanie poprawne')
        return True
    else:
        print('Logowanie niepoprawne')
        return False

hasla_niedozwolone = ['kamil123', 'marysia123', '1234', '12345']
users = {'KamilM' : 'qwe', 'Basia': 'stonoga', 'Gargamel': 'gargamel1'}

while True:
    print('Witamy w programie\nCo chcesz zrobic?\n')
    print('1. sprawdzić, czy proponowane haslo jest dozwolone')
    print('2. dodać użytkownika')
    print('3. zmiane hasla')
    print('4. usunac uzytkownika')
    print('5. usunac wszystkich uzytkownikow')
    print('6. wyjsc z programu')
    wybor = int(input())

    if wybor == 1:
        password = input('Wpisz haslo:  ')
        is_password_allowed(password)

    elif wybor == 2:
        if logging():
            new_password = input('Wpisz nowe haslo:  ')
            if is_password_allowed(new_password):
               users[user] = password  #nowe hasło
               print(users)
            else:
            print('uzytkownik juz istnieje badź haslo niedozwolone')

    elif wybor == 3:
        user = input('Wpisz nazwe uzytkownika:  ')
        password = input('Wpisz haslo:  ')
        if user in users and password == users[user]:
            new_password = input('Wpisz nowe haslo:  ')
            if is_password_allowed(new_password):
                users[user] = new_password
        else:
            print('blad')
        print(users)

    elif wybor == 4:
        user = input('Wpisz nazwe uzytkownika:  ')
        password = input('Wpisz haslo:  ')
        if user in users and password == users[user]:
            del users[user]
        print(users)

    elif wybor == 5:
        user = input('Wpisz nazwe uzytkownika:  ')
        password = input('Wpisz haslo:  ')
        if user == 'KamilM' and password == users[user]:
            users.clear()

    elif wybor == 6:
        break

    else:
        print('zly wybor')
        break

print('koniec programu')
