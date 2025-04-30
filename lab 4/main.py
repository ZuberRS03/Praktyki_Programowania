# Podsystemy – klasy wewnętrzne
class Engine:
    def start(self):
        print("Silnik uruchomiony.")

class AirConditioning:
    def turn_on(self):
        print("Klimatyzacja włączona.")

class Radio:
    def set_station(self, station):
        print(f"Radio ustawione na stację: {station}")


# Fasada – pojedynczy, uproszczony interfejs
class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.ac = AirConditioning()
        self.radio = Radio()

    def start_trip(self):
        print("Przygotowanie do podróży...")
        self.engine.start()
        self.ac.turn_on()
        self.radio.set_station("RMF FM")
        print("Samochód gotowy do jazdy!")


# Klient – korzysta z uproszczonego interfejsu
if __name__ == "__main__":
    car = CarFacade()
    car.start_trip()
