class Auto:
    def __init__(self, vin_number: int, kolor='red', info_o_kondycji=4):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self._kondycja = info_o_kondycji
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.__vin_number = vin_number

    def __str__(self):
        return f'Obiekt klasy Auto, kolor {self.kolor}'

    def wlacz_eco(self):
        self.tryb_ekonomiczny = True
        self.spalanie_na_100 = 9
        print('\n.......Tryb ECO wlaczony........\n')

    def wlacz_normal(self):
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        print('\n.......Tryb NORMAL wlaczony........\n')

    def zmien_tryb(self, tryb):
        if tryb == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 9
            print('\n.......Tryb ECO wlaczony........\n')
        elif tryb == 'normal':
            self.wlacz_normal()   # jedna metoday wywołuje drugą
        else:
            print('nierozpoznany wybor, brak zmian')

    def zasieg(self):
        max_dystans = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        print(f'paliwo skonczy sie za {round(max_dystans)} km.')
        if max_dystans < 20:
            print(f'UWAGA, tankowanie potrzebne')

    def wyswietl_vin(self):
        print(self.__vin_number)


class Pracownik:
    def __init__(self):
        self.imie = 'Jan'
        self.nazwisko = 'Kowalski'
        self.kolor = 'brak'

    def przedstaw(self):
        print(f'Hej, nazywam sie {self.imie}')

worker1 = Pracownik()
auto_kamila = Auto(12345, 'blue', 3)
auto_kamila.zmien_tryb('eco')
auto_kamila.zasieg()
auto_lukasza = Auto(12456)
print(auto_kamila.kolor)
auto_lukasza.tryb_ekonomiczny = True
print(auto_lukasza.tryb_ekonomiczny)
auto_lukasza.wlacz_eco()
print(f'spalanie wynosi ',auto_lukasza.spalanie_na_100)
auto_kamila.zmien_tryb('eco')
auto_kamila._Auto__vin_number = 100
auto_kamila.__vin_number = 200

print(auto_kamila._Auto__vin_number)

print(auto_kamila)




