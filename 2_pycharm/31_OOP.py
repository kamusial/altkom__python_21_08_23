class Ptak:
    def __init__(self, gatunek: str, predkosc: int):
        self.gatunek = gatunek
        self.predkosc = predkosc

    def lec(self):
        print(f'Gatunek {self.gatunek}. Osiagam predkosc {self.predkosc} km/h')

    def daj_glos(self):
        print('play sound.mp3')


class Papuga(Ptak):
    def __init__(self, szybkosc, kolor):
        super().__init__('papuga', szybkosc)
        self.szybkosc = szybkosc
        self.kolor = kolor

    def dziub(self):
        print('wykonana animacja dziubanie.gif')

    def daj_glos(self):
        print('play gadanie.mp3')

obiekt1 = Ptak('gat', 25)
obiekt2 = Papuga(24, 'zielony')
print(obiekt2.gatunek)
print(obiekt2.kolor)
obiekt1.daj_glos()
obiekt2.daj_glos()