import time
import psutil

ts1 = time.time()

lista = tuple(range(0, 10000000))
dlugosc = len(lista)
#print(len(lista))
print('The CPU usage is: ', psutil.cpu_percent(4))
for i in lista:
    if True:
        pass

#print(lista)
#
# if dlugosc < 1000:
#     print(f'krotka lista')
# elif dlugosc < 10000:
#     print(f'srednia lista')
# elif dlugosc < 100000:
#     print(f'i tak srednia lista')

ts2 = time.time()
print(f'czas {ts2 - ts1}')

# ts1 = time.time()
# print(len(lista))
# ts2 = time.time()
# print(f'czas {ts2 - ts1}')