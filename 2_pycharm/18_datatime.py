import datetime
import time


def filename(name, extention):
    current_time = datetime.datetime.now()
    return name + current_time.strftime('_%H%M%S') + '.' + extention


#funkcja wypisująca nazwy plikow z aktualnym czasem
for i in range (10):
    print(filename('kamil', 'txt'))
    time.sleep(2)

now = datetime.datetime.now()    #wyciągnięcie czasu z systemu
print(type(now))
print(now)

timer = now.strftime('%H:%M:%S')       #stworzenie godziny w żądanym formacie
date = now.strftime('year = %Y, month = %m, day = %d')
print(timer)
print(date)


